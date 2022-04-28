import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import tkinter.ttk as ttk
import os

import pandas as pd


if __name__ == "__main__":
    print('start project')
    # app = App()
    # app.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Інформаційно-пошукова система \"Електронна фільмотека\"")
        self.maxsize(1024, 700)
        self.iconbitmap('oscar.ico')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.filter = "1"
        # 1 - весь список
        # 2 - за роком створення
        # 3 - за країною
        # 4 - за жанром
        self.country_filter = "США"
        self.year_filter = 1997
        self.before_filter = True
        self.genre_filter = 'драма'

    # функція закриття головного вікна програми
    def on_closing(self):
        if mb.askokcancel("Вихід", "Ви дійсно бажаєте вийти?"):
            self.curs.close()
            self.conn.close()
            self.destroy()