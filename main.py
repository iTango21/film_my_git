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

    # функція відкриття вікна "Про програму"
    def open_about(self):
        about_dialog = about.About(self)
        about_dialog.grab_set()

    # функція відкриття вікна "Допомога"
    def open_help(self):
        os.startfile("helppp.pdf")

    # функція відкриття вікна ":: Друк елемента ::"
    def print_elem(self):
        # Відкриття файлу виводу reselem.html
        select = self.tree.item(self.tree.selection())['values']
        if not (select):
            mb.showerror(":: Друк елемента ::", "Виберіть фільм!")
            return
        try:
            fout = open('reselem.html', 'wt')
        except:
            mb.showinfo('Помилка', 'Неможливо створити файл виводу!!!')
            return
        print('<html><head><title>Інформація про фільм</title></head><body>', file=fout)
        print('<p>Назва фільму: {}</p>'.format(select[0]), file=fout)
        print('<p>Країна: {}</p>'.format(select[1]), file=fout)
        print('<p>Жанр: {}</p>'.format(select[2]), file=fout)
        print('<p>Рік: {}</p>'.format(select[3]), file=fout)
        print('<p>Режисер: {}</p>'.format(select[4]), file=fout)
        print('<p>Оскар: {}</p>'.format(select[5]), file=fout)
        print('</body></html>', file=fout)
        fout.close()
        os.startfile("reselem.html")

    # функція відкриття вікна "Довідник країн"
    def open_country(self):
        count_dialog = country_dov.CountDov(self)
        count_dialog.grab_set()

    # функція відкриття вікна "Довідник жанрів"
    def open_genre(self):
        genre_dialog = genredov.GenreDov(self)
        genre_dialog.grab_set()

    # функція закриття головного вікна програми
    def on_closing(self):
        if mb.askokcancel("Вихід", "Ви дійсно бажаєте вийти?"):
            self.curs.close()
            self.conn.close()
            self.destroy()

            if __name__ == "__main__":
                app = App()
                app.mainloop()

            if __name__ == "__main__":
                print("Запускайте файл main.py")