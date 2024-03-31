import csv

def look(key):
    for i in key:
            if i in '0123456789':
                pass
            else:
                print('non number found')
                return True
    return False

def get_file(file_name):
    diction = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for rows in reader:
            key, value = rows
            diction[key] = value

    return diction

def main():
    file = 'students.csv'
    data = get_file(file)

    key = input('enter key')

    if len(key) > 9:
        print('to big')
    elif len(key) < 9:
        print('to small')
    elif look(key):
        pass
    else:
        print(data[key])

if __name__ == '__main__':
    main()
