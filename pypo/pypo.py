from tkinter import Tk

from pypo.gui import GUI

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300')
    my_gui = GUI(root)
    root.mainloop()
