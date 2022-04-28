import tkinter as tk

class YearFilter(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("За роком створення")
        self.resizable(0, 0)
        self.year = tk.StringVar()
        self.label1 = tk.Label(self, text="Вивести всі фільми, відзняті")

        self.frame1 = tk.Frame(self)
        self.var = tk.IntVar()
        self.rbutton1 = tk.Radiobutton (self.frame1, text = 'до', variable = self.var, value = 1)
        self.rbutton2 = tk.Radiobutton (self.frame1, text = 'після', variable = self.var, value = 2)

        self.frame2 = tk.Frame(self)
        self.year1 = tk.Entry(self.frame2, width = 15, textvariable = self.year)
        self.label2 = tk.Label(self.frame2, text="року")

        self.frame3 = tk.Frame(self)
        self.ok = tk.Button(self.frame3, text = "Прийняти", command = self.save)
        self.cancel = tk.Button(self.frame3, text = "Скасувати", command = self.leave)

        self.label1.pack(padx = 70, pady = 10)
        self.frame1.pack(padx = 10, pady = 10)
        self.rbutton1.grid(row = 0, column = 0, padx = 5)
        self.rbutton2.grid(row = 0, column = 1, padx = 5)

        self.frame2.pack(padx = 10, pady = 10)
        self.year1.grid(row = 0, column = 0, padx = 5)
        self.label2.grid(row = 0, column = 1, padx = 5)

        self.frame3.pack(padx = 10, pady = 10)
        self.ok.grid(row = 0, column = 0, padx = 10, ipadx = 10)
        self.cancel.grid(row = 0, column = 1, padx = 10, ipadx = 5)

    def leave(self):
        self.year1.delete(0, tk.END)
        self.destroy()

    def save(self):
        self.destroy()
        return (self.year.get(),
                self.var.get())


if __name__ == "__main__":
    print("Запускайте файл main.py")
