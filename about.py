import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Про програму")
        self.resizable(0, 0)
        self.frame = tk.LabelFrame(self, height=200, width=400, padx=30,
                                   pady=30)
        self.image = Image.open("oscar.png")
        self.image = self.image.resize((50, 140), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label0 = tk.Label(self.frame, image=self.photo)
        self.label1 = tk.Label(self.frame, text="Інформаційно-пошукова система")
        self.label2 = tk.Label(self.frame, text="\"Електронна фільмотека\"")
        self.label3 = tk.Label(self.frame, text="Copyright (C) 2022")
        self.ok = tk.Button(self, text="ОК", command=self.destroy)

        self.frame.pack(padx=10, pady=5)
        self.label0.grid(row=0, column=0, rowspan=3, padx=5)
        self.label1.grid(row=0, column=1, pady=5)
        self.label2.grid(row=1, column=1, pady=5)
        self.label3.grid(row=2, column=1, pady=5)

        self.ok.pack(padx=5, pady=10, ipadx=15)


if __name__ == "__main__":
    print("Запускайте файл main.py")