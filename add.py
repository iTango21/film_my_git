import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb

import csv

with open("csv_db.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            country_ = row
            count += 1
        else:
            genre_ = row

# print(country_)
# breakpoint()

class Add(tk.Toplevel):
    def __init__(self, parent, name, country, year, director, genre, oscar):
        super().__init__(parent)
        self.title("Додавання фільму")
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # name;country;genre;year;director;oscars;rating;

        self.name = tk.StringVar()
        self.country = tk.StringVar()
        self.year = tk.StringVar()
        self.director = tk.StringVar()
        self.genre = tk.StringVar()
        self.oscar = tk.StringVar()
        #   name;country;genre;year;director;oscars
        #   Назва Країна Жанр Рік Режисер Оскар(к-ть)
        self.label = tk.Label(self, text="Введіть інформацію про фільм")
        self.namelabel = tk.Label(self, text="Назва фільму")
        self.nameedit = tk.Entry(self, width=30, textvariable=self.name)
        self.countrylabel = tk.Label(self, text="Країна")
        self.countrycombobox = ttk.Combobox(self, width=27,
                                            height=5, textvariable=self.country)
        self.countrycombobox['values'] = country_
        # -------------------------------------
        self.genrelabel = tk.Label(self, text="Жанр")
        self.genrecombobox = ttk.Combobox(self, width=27,
                                          height=5, textvariable=self.genre)
        self.genrecombobox['values'] = genre_
        #-------------------------------------
        self.yearlabel = tk.Label(self, text="Рік")
        self.yearedit = tk.Entry(self, width=30, textvariable=self.year)
        self.directorlabel = tk.Label(self, text="Режисер")
        self.directoredit = tk.Entry(self, width=30, textvariable=self.director)

        self.oscarlabel = tk.Label(self, text="Оскар")
        self.oscaredit = tk.Entry(self, width=30, textvariable=self.oscar)
        self.ok = tk.Button(self, text="Прийняти", command=self.ok)
        self.cancel = tk.Button(self, text="Скасувати",
                                command=self.cancel)
        self.label.grid(row=0, column=0, columnspan=2,
                        padx=50, pady=20)
        self.namelabel.grid(row=1, column=0, pady=10, padx=10,
                            sticky=tk.E)
        self.nameedit.grid(row=1, column=1, pady=10, padx=10)
        self.countrylabel.grid(row=2, column=0, pady=10, padx=10,
                               sticky=tk.E)
        self.countrycombobox.grid(row=2, column=1, pady=10, padx=10)
        self.genrelabel.grid(row=3, column=0, pady=10, padx=10,
                             sticky=tk.E)
        self.genrecombobox.grid(row=3, column=1, pady=10, padx=10)
        self.yearlabel.grid(row=4, column=0, pady=10, padx=10,
                            sticky=tk.E)
        self.yearedit.grid(row=4, column=1, pady=10, padx=10)
        self.directorlabel.grid(row=5, column=0, pady=10, padx=10,
                              sticky=tk.E)
        self.directoredit.grid(row=5, column=1, pady=10, padx=10)
        self.oscarlabel.grid(row=6, column=0, pady=10, padx=10,
                                sticky=tk.E)
        self.oscaredit.grid(row=6, column=1, pady=10, padx=10)
        self.ok.grid(row=7, column=0, pady=20, ipadx=10,
                     padx=20, sticky=tk.W)
        self.cancel.grid(row=7, column=1, pady=20, ipadx=10,
                         padx=20, sticky=tk.E)
        self.nameedit.insert(0, name)
        self.directoredit.insert(0, director)
        self.yearedit.insert(0, year)
        self.countrycombobox.insert(0, country)
        self.genrecombobox.insert(0, genre)
        self.oscaredit.insert(0, oscar)


if __name__ == "__main__":
    print("Запускайте файл main.py")