#Imports
import tkinter
import csv


#File functions
def read_file(filename):
    data = {}
    try:
        with open(filename, 'r') as datafile:
            datareader = csv.reader(datafile)
            next(datareader)
            for a, b, c in datareader:
                data[a] = [a, b, c]
    except FileNotFoundError:
        print('Error! File Not Found.')
    finally:
        return data

def write_file(data, filename):
    with open(f'{filename}.csv', 'w') as savefile:
        writer = csv.writer(savefile, delimiter = ',')
        writer.writerow(['Product #','Quantity'])
        for key in data.keys():
            writer.writerow([key, data[key]])

#Classes
class ItemCart(): #this has been tested
    holder = {}
    estiment = 0
    file = False
    
    def __init__(self):...

    def find(self, key):
        if key in self.holder.keys():
            return True
        else:
            return False

    def add(self, item, quantity):
        key, name, price = item
        if self.find(key):
            self.holder[key] += quantity
            self.estiment += float(price) * quantity
        else:
            self.holder[key] = quantity
            self.estiment += float(price) * quantity
        return self.holder[key]

    def remove(self, item, quantity):
        key, name, price = item
        if self.find(key):
            if self.holder[key] > quantity:
                self.holder[key] -= quantity
                self.estiment -= float(price) * quantity
                return self.holder[key]

            elif self.holder[key] == quantity:
                del self.holder[key]
                self.estiment -= float(price) * quantity
                return 0

            elif self.holder[key] < quantity:
                self.estiment -= float(price) * self.holder[key]
                del self.holder[key]
                return 0

    def submit(self):
        write_file(self.holder, 'Item_request')
        self.file = True
        self.holder = {}
        self.update()

    def report(self):
        print(self.holder)
        print(self.estiment)

    def report_labels(self, root, y):
        self.holder_label = tkinter.Label(
            root, text = f'0 Items in cart')
        self.holder_label.grid(row = y, column = 0)

        self.estiment_label = tkinter.Label(
            root, text = f'Estimated cost $0')
        self.estiment_label.grid(row = y, column = 2)

        self.file_label = tkinter.Label(
            root, text = '')
        self.file_label.grid(row = y, column = 5)

    def button(self, root, y):
        self.button = tkinter.Button(
            root, text = 'Submit', command = self.submit)
        self.button.grid(row = y, column = 4)

    def update(self):
        items = 0
        for key in self.holder.keys():
            items += self.holder[key]
        if items == 0:
            self.estiment = 0

        if self.file:
            self.file_label.config(text = 'Your File has been submited')
        self.holder_label.config(text = f'{items} Items in cart')
        self.estiment_label.config(text = f'Estimated cost ${self.estiment: .2f}')
        

class ItemLine():

    def __init__(self, root, cart, item, y = 0):
        self.root = root
        self.item = item
        self.cart = cart
        self.y = y
        self.build_labels()
        self.build_entrys()
        self.build_buttons()

    def add(self):
        try:
            q = int(self.entry_in.get())
        except ValueError:
            q = 0
        num = self.cart.add(self.item, q)
        self.label_2.config(text = f'{num} items in cart')
        self.cart.update()

    def remove(self):
        try:
            q = int(self.entry_out.get())
        except ValueError:
            q = 0
        num = self.cart.remove(self.item, q)
        self.label_2.config(text = f'{num} items in cart')
        self.cart.update()

    def build_labels(self):
        self.label_1 = tkinter.Label(
            self.root, text = f'{self.item[1]} @ {self.item[2]} each')
        self.label_1.grid(row = self.y, column = 0)

        self.label_2 = tkinter.Label(
            self.root, text = f'0 items in cart')
        self.label_2.grid(row = self.y, column = 3)

    def build_entrys(self):
        self.entry_in = tkinter.Entry(
            self.root)
        self.entry_in.grid(row = self.y, column = 1)

        self.entry_out = tkinter.Entry(
            self.root)
        self.entry_out.grid(row = self.y, column = 4)

    def build_buttons(self):
        self.button_in = tkinter.Button(
            self.root, text = f'Add to Cart', command = self.add)
        self.button_in.grid(row = self.y, column = 2)

        self.button_out = tkinter.Button(
            self.root, text = f'Remove from Cart', command = self.remove)
        self.button_out.grid(row = self.y, column = 5)

#Main Function
def main(): 
    root = tkinter.Tk()
    root.title('Shopping Cart')
    root.geometry('800x500')

    stock = read_file('products.csv')
    cart = ItemCart()
    lines = []

    for key in stock.keys():
        lines.append(ItemLine(root, cart, stock[key], len(lines)))
    cart.report_labels(root, len(lines))
    cart.button(root, len(lines))

if __name__ == '__main__':
    main()
