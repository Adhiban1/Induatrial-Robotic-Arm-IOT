from tkinter import *

root = Tk()


def main(a):
    print(a)


root.bind("<Key>", main)

root.mainloop()

