"""Python Portage."""
from pprint import pprint
from tkinter import Label, Button, Tk

from pypo.emerge import read_dtat


class GUI:
    """Python Portage GUI in tkinter."""
    def __init__(self, master: Tk) -> None:
        """
        Basic initialization.

        :param master: root widget
        """
        self.root = master
        self.root.title('A simple GUI')

        self.label = Label(self.root, text='This is our first GUI!')
        self.label.pack()

        self.greet_button = Button(self.root, text='Greet', command=GUI.greet)
        self.greet_button.pack()

        self.close_button = Button(self.root, text='Close', command=self.root.quit)
        self.close_button.pack()

    @staticmethod
    def greet() -> None:
        """Just show debug data to console."""
        with open('../e01.txt') as emerge_log:
            records_from_file = emerge_log.read()

        database = read_dtat(records_from_file)
        pprint(database)
