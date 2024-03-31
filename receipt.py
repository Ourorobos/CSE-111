""" To exceed the requirements I added some code so that
if you order an even amount of total items and end up on
a even amount of dollars not including the cents you get
a 5% discount"""


import csv
import datetime

files = ['products.csv','request.csv']

def print_receipt(item_list, length, subtotal, d1, d2, tax, total):
    cdt = datetime.datetime.now()
    print('Store Name \n')
    for a, b, c in item_list:
        print(f'{a}: {c} @ {b}')
    print(f'\nTotaling {length} Items')
    print(f'Subtotal: {round(subtotal,2)}')
    print(f'Discount: -{round(d1,2)}')
    print(f'Subtotal: {round(d2,2)}')
    print(f'Sales Tax: {round(tax,2)}')
    print(f'Total: {round(total,2)} \n')
    print("Thanks for Shopping at 'Store Name'! Please come again.")
    try:
        cdt = datetime.datetime.now(tz=None)
        print(f'Current Date & Time : {cdt: %a %b %d, %Y %I:%M:%S %p}')
    except:
        print('Curret Date & Time : ERROR')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            diction = {}
            next(reader)
            for row in reader:
                diction[row[key_column_index]] = row
            return diction

    except FileNotFoundError:
        print(f'{filename} Was Not Found')
        return False

def main():
    products_dict = read_dictionary(files[0],0)
    item_list = []
    subtotal, length, d1, d2 = 0,0,0,0

    try:
        with open(files[1],'r') as file:
            reader = csv.reader(file)
            next(reader)
            for ids, q in reader:
                try:
                    pro_ids, pro_name, pro_price = products_dict[ids]
                    q, pro_price = int(q), float(pro_price)
                    item_list.append([pro_name, pro_price, q])
                    length += q
                    subtotal += pro_price * q
                except KeyError:
                    print(f'Error: unknown product Id [{ids}]')
                    return False
                except TypeError:
                    print('Failed to get dictionary')
                    return False
    except FileNotFoundError:
        print(f'{files[1]} Was Not Found')
        return False

    #exceeding requiremens code block
    if length%2 == 0 and int(subtotal)%2 == 0:
        d1 = subtotal * 0.05
        d2 = subtotal - d1
    else:
        d2 = subtotal

    tax = d2 * 0.06
    total = d2 + tax

    print_receipt(item_list, length, subtotal, d1, d2, tax, total)

if __name__ == '__main__':
    main()
