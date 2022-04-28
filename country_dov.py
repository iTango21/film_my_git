import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb

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


def file_write():
    with open("csv_db.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            country
        )
        writer.writerow(
            genre
        )


class CountDov(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Довідник країн")
        self.resizable(0, 0)

        self.frame = tk.Frame(self, height=200, width=400, padx=5,
                              pady=5)
        self.frame2 = tk.Frame(self, height=50, width=400, padx=5,
                               pady=5)

        self.scrollbar = tk.Scrollbar(self.frame)

        self.listbox = tk.Listbox(self.frame, height=10, width=30, selectmode=tk.SINGLE,
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        for elem in country:
            self.listbox.insert(tk.END, elem)

        self.add = tk.Button(self.frame2, text="  Додати  ", command=self.open_add)
        self.edit = tk.Button(self.frame2, text="Редагувати", command=self.open_edit)
        self.dell = tk.Button(self.frame2, text=" Видалити ", command=self.open_del)

        self.frame.grid(row=0, column=0, padx=5, pady=5)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.frame2.grid(row=0, column=1, padx=5, pady=5)

        self.add.grid(row=0, column=0, padx=15, pady=10, ipadx=20)
        self.edit.grid(row=1, column=0, padx=15, pady=10, ipadx=15)
        self.dell.grid(row=2, column=0, padx=15, pady=10, ipadx=16)


if __name__ == "__main__":
    print("Запускайте файл main.py")