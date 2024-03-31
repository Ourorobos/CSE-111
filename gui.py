import tkinter
import random

def func():
    try:
        user_a, user_b = int(objs[2].get()), int(objs[4].get())
        if user_a > user_b:
            num = random.randint(user_b, user_a)
        elif user_a == user_b:
            num = 'no'
        else:
            num = random.randint(user_a, user_b)
    except ValueError:
        num = 'Enter Numbers Only'
    finally:
        objs[-1].config(text = f'Random number: {num}')

def main():
    root = tkinter.Tk()
    root.title('GUI.PY')
    root.geometry('500x250')

    global objs
    objs = [
    tkinter.Label(root, text = 'Enter two diffrent numbers'),
    tkinter.Label(root, text = 'Number One:'),
    tkinter.Entry(root),
    tkinter.Label(root, text = 'Number Two:'),
    tkinter.Entry(root),
    tkinter.Button(root, text = 'Get Number', command = func),
    tkinter.Label(root, text = f'Random number:'),
    ]

    for obj in objs:
        obj.grid(row = objs.index(obj), column = 0)

    root.mainloop()

if __name__ == '__main__':
    main()
