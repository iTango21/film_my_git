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
