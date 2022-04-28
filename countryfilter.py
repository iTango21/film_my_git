import tkinter as tk
import tkinter.ttk as ttk

import csv

with open("csv_db.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            country = row
            count += 1
        else:
            genre = row


class CountryFilter(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("За країною")
        self.resizable(0, 0)

        self.country = tk.StringVar()
        self.label1 = tk.Label(self, text="Фільми відзняті країною:")

        self.countrycombobox = ttk.Combobox(self, width=27,
                                          height=5, textvariable=self.country)

        self.countrycombobox['values'] = country

        self.frame = tk.Frame(self)
        self.ok = tk.Button(self.frame, text="Прийняти", command=self.save)
        self.cancel = tk.Button(self.frame, text="Скасувати", command=self.leave)

        self.label1.pack(padx=70, pady=10)
        self.countrycombobox.pack(padx=10, pady=10)

        self.frame.pack(padx=10, pady=10)
        self.ok.grid(row=0, column=0, padx=10, ipadx=10)
        self.cancel.grid(row=0, column=1, padx=10, ipadx=5)

    def leave(self):
        self.countrycombobox.delete(0, tk.END)
        self.destroy()

    def save(self):
        self.destroy()
        return self.country.get()


if __name__ == "__main__":
    print("Запускайте файл main.py")

