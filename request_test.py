#Imports
import pytest

from request import ItemCart

#test "items" item_id, item_name, item_price
test_items = [
    ['a1', 'Apple', 0.5],
    ['b1', 'Banana', 0.75],
    ['c1', 'Cat Food', 25.99],
    ['c2', 'Cat Litter', 15.99],
    ['d1', 'Detergent', 11.11],
    ]

def test_itemcart_add():
    cart = ItemCart()
    cart.add(test_items[0], 5)
    assert cart.estiment == test_items[0][2] * 5
    assert cart.holder[test_items[0][0]] == 5

    cart = ItemCart()
    cart.add(test_items[2], 1)
    assert cart.estiment == test_items[2][2] * 1
    assert cart.holder[test_items[2][0]] == 1  

def test_itemcart_remove():
    cart = ItemCart()
    #filling the cart
    cart.add(test_items[1],3)
    cart.add(test_items[3],5)
    cart.add(test_items[4],1)
    mem = cart.estiment

    cart.remove(test_items[1],1)
    mem -= test_items[1][2]
    assert cart.estiment == mem
    assert cart.holder[test_items[1][0]] == 2

    cart.remove(test_items[3],5)
    mem -= test_items[3][2] * 5
    assert cart.estiment == mem
    assert test_items[3][0] not in cart.holder.keys()

    cart.remove(test_items[4],1)
    mem -= test_items[4][2]
    assert cart.estiment == mem
    assert test_items[4][0] not in cart.holder.keys()

def main():
    pytest.main(["-v", "--tb=line", "-rN", __file__])


if __name__ == '__main__':
    main()
