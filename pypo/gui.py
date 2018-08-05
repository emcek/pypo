"""Python Portage."""
from logging import DEBUG, getLogger, StreamHandler, Formatter, Logger
from pprint import pformat
from tkinter import Label, Button, Tk

from pypo.emerge import parse


class GUI:
    """Python Portage GUI in tkinter."""

    def __init__(self, master: Tk) -> None:
        """
        Basic initialization.

        :param master: root widget
        """
        self.log = GUI.set_logger()

        self.root = master
        self.root.title('A simple GUI')

        self.label = Label(self.root, text='This is our first GUI!')
        self.label.pack()

        self.greet_button = Button(self.root, text='Greet', command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(self.root, text='Close', command=self.root.quit)
        self.close_button.pack()

    def greet(self) -> None:
        """Just show debug data to console."""
        with open('../e01.txt') as emerge_log:
            records_from_file = emerge_log.read()

        database = parse(records_from_file)
        self.log.debug(pformat(database))
        self.log.info(len(database))

    @staticmethod
    def set_logger() -> Logger:
        """
        Setup of logger.

        :return: instance of configured logger
        """
        log = getLogger(__name__)
        log.setLevel(DEBUG)
        ch = StreamHandler()
        ch.setLevel(DEBUG)
        ch.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        log.addHandler(ch)
        return log
