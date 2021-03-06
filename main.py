import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import tkinter.ttk as ttk
import os

import pandas as pd
df = pd.read_csv('movie5.csv', sep=';', header=0)

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

        self.radio = tk.StringVar()
        self.radio.set("1")

        # # головне меню
        menu = tk.Menu(self)

        dov_menu = tk.Menu(menu, tearoff=0)
        dov_menu.add_command(label="Довідник країн", command=self.open_country)
        dov_menu.add_command(label="Довідник жанрів", command=self.open_genre)

        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Додати", command=self.open_add)
        edit_menu.add_command(label="Видалити", command=self.open_del)
        edit_menu.add_command(label="Коригувати", command=self.open_edit)

        self.img_find = tk.PhotoImage(file='find_36.png')
        find_menu = tk.Menu(menu, tearoff=0)
        find_menu.add_command(image=self.img_find, command=self.open_find)
        menu.add_cascade(label="Пошук", menu=find_menu)

        filter_menu = tk.Menu(menu, tearoff=0)
        filter_menu.add_radiobutton(label="Весь список", value="1",
                                    variable=self.radio, command=self.filter_all)
        filter_menu.add_radiobutton(label="За роком створення", value="2",
                                    variable=self.radio, command=self.filter_year)
        filter_menu.add_radiobutton(label="За країною", value="3",
                                    variable=self.radio, command=self.filter_country)
        filter_menu.add_radiobutton(label="За жанром", value="4",
                                    variable=self.radio, command=self.filter_genre)

        print_menu = tk.Menu(menu, tearoff=0)
        print_menu.add_command(label="Друк елемента", command=self.print_elem)
        print_menu.add_command(label="Роздрукувати список", command=self.print_list)

        about_menu = tk.Menu(menu, tearoff=0)
        about_menu.add_command(label="Про програму", command=self.open_about)
        about_menu.add_separator()
        about_menu.add_command(label="Довідка", command=self.open_help)

        menu.add_cascade(label="Довідники", menu=dov_menu)
        menu.add_cascade(label="Редагування", menu=edit_menu)
        menu.add_cascade(label="Фільтр", menu=filter_menu)
        menu.add_cascade(label="Друк", menu=print_menu)

        menu.add_cascade(label="?", menu=about_menu)

        self.config(menu=menu)

        #   name;country;genre;year;director;oscars
        #   Назва Країна Жанр Рік Режисер Оскар(к-ть)
        columns = ("#1", "#2", "#3", "#4", "#5", "#6")
        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        self.tree.heading("#1", text="Назва")
        self.tree.column("#1", minwidth=100, width=200)
        self.tree.heading("#2", text="Країна")
        self.tree.column("#2", minwidth=100, width=200)
        self.tree.heading("#3", text="Жанр")
        self.tree.column("#3", minwidth=50, width=100)
        self.tree.heading("#4", text="Рік")
        self.tree.column("#4", minwidth=100, width=150)
        self.tree.heading("#5", text="Режисер")
        self.tree.column("#5", minwidth=100, width=150)
        self.tree.heading("#6", text="Оскар")
        self.tree.column("#6", minwidth=100, width=150)
        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.W)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.status = tk.Label(self, text=f" Фільтр: весь список.", bd=1, relief=tk.SUNKEN,
                               anchor=tk.W)
        self.status.grid(row=1, column=0, columnspan=2, pady=1, padx=1,
                         sticky=tk.E + tk.W)

        df = pd.read_csv('movie5.csv', sep=';', header=0)
        df = df.sort_values(by='name', ascending=True)

        for elem in df.values.tolist():
            self.tree.insert("", tk.END, values=elem)

    # функція виведення списку фільмів з фільтруванням
    def view(self):
        self.tree.delete(*self.tree.get_children())
        if self.filter == "1":
            df = pd.read_csv('movie5.csv', sep=';', header=0)
            df = df.sort_values(by='name', ascending=True)
            self.status['text'] = " Фільтр: весь список"
        elif self.filter == "2":
            s = " Фільтр: за роком створення"
            if self.before_filter:
                df = pd.read_csv('movie5.csv', sep=';', header=0)
                df = df.loc[df["year"] < self.year_filter].head()
                s = s + " - до "
            else:
                df = pd.read_csv('movie5.csv', sep=';', header=0)
                df = df.loc[df["year"] > self.year_filter].head()
                s = s + " - після "
            s = s + str(self.year_filter) + " року"
            self.status['text'] = s
        elif self.filter == "3":
            df = pd.read_csv('movie5.csv', sep=';', header=0)
            df = df.loc[df["country"] == self.country_filter].head()
            self.status['text'] = " Фільтр: за країною - " + self.country_filter
        elif self.filter == "4":
            df = pd.read_csv('movie5.csv', sep=';', header=0)
            df = df.loc[df["genre"] == self.genre_filter].head()
            self.status['text'] = " Фільтр: за жанром - " + self.genre_filter

        for elem in df.values.tolist():
            self.tree.insert("", tk.END, values=elem)


    # функція фільтрування - весь список
    def filter_all(self):
        self.filter = self.radio.get()
        self.view()

    # функція фільтрування - за роком створення
    def filter_year(self):
        filt = self.radio.get()
        year_dialog = yearfilter.YearFilter(self)
        year_dialog.grab_set()
        year_dialog.wait_window()
        year = year_dialog.save()
        if not (year[0]):
            self.radio.set(self.filter)
            return
        self.year_filter = int(year[0])
        if year[1] == 1:
            self.before_filter = True
        else:
            self.before_filter = False
        self.filter = filt
        self.view()

    # функція фільтрування - за країною
    def filter_country(self):
        filt = self.radio.get()
        country_dialog = countryfilter.CountryFilter(self)
        country_dialog.grab_set()
        country_dialog.wait_window()
        country = country_dialog.save()
        if not (country):
            self.radio.set(self.filter)
            return
        self.country_filter = country
        self.filter = filt
        self.view()

    # функція фільтрування - за жанром
    def filter_genre(self):
        filt = self.radio.get()
        genre_dialog = genrefilter.GenreFilter(self)
        genre_dialog.grab_set()
        genre_dialog.wait_window()
        genre = genre_dialog.save()
        if not (genre):
            self.radio.set(self.filter)
            return
        self.genre_filter = genre
        self.filter = filt
        self.view()

    # функція відкриття вікна "Додавання фільму"
    def open_add(self):
        add_dialog = add.Add(self, '', '', '', '', '', '')
        add_dialog.grab_set()
        add_dialog.wait_window()
        film = add_dialog.save()
        if not (film[0]):
            return
        aaa = df.loc[df['name'].str.contains(film[0], case=False)]
        if aaa.empty:
            print(film)
            df.loc[len(df.index)] = [film[0], film[1], film[2], film[3], film[4], film[5]]
            df.to_csv('movie5.csv', sep=';', index=False)
        else:
            mb.showinfo("Увага!", "Такий фільм вже існує!")
        self.view()

    # функція відкриття вікна "Редагування фільму"
    def open_edit(self):
        select = self.tree.item(self.tree.selection())['values']

        if not (select):
            mb.showerror("Коригування.", "Виберіть фільм!")
            return

        add_dialog = add.Add(self, select[0], select[1], select[3], select[4], select[2], select[5])
        add_dialog.grab_set()

        add_dialog.wait_window()
        film = add_dialog.save()

        if not (film[0]):
            return
        if mb.askokcancel("Коригування", "Ви дійсно бажаєте внести зміни в інформацію про фільм "
                                         + str(select[0]) + "?"):
            df_edit = pd.read_csv("movie5.csv", sep=';', index_col="name")
            df_edit.drop([select[0]], inplace=True)
            df_edit.to_csv('movie5.csv', sep=';')
            df = pd.read_csv('movie5.csv', sep=';', header=0)
            df.loc[len(df.index)] = [film[0], film[1], film[2], film[3], film[4], film[5]]
            df.to_csv('movie5.csv', sep=';', index=False)
            self.view()

    # функція відкриття вікна "Видалення фільму"
    def open_del(self):
        select = self.tree.item(self.tree.selection())['values']
        if select[0]:
            if mb.askokcancel("Видалення", "Ви дійсно бажаєте видалити фільм "
                                           + str(select[0]) + "?"):
                df = pd.read_csv("movie5.csv", sep=';', index_col="name")
                df.drop([select[0]], inplace=True)
                df.to_csv('movie5.csv', sep=';')
                self.view()
        else:
            mb.showerror("Помилка!", "Запис відсутній")

    # функція відкриття вікна "Пошук"
    def open_find(self):
        name = sd.askstring("Пошук", "Введіть назву фільму:")
        aaa = df.loc[df['name'].str.contains(name, case=False)]
        if aaa.empty:
            mb.showerror("Помилка!", "Такого фільму не існує!")
        else:
            find_info = df.loc[df['name'].str.contains(name, case=False)].values

            info = "Назва: \t{0}\n\nКраїна: \t{1}\n\nЖанр: \t{2}\n\nРік: \t{3}\n\nРежисер: {4}\n\nОскар: \t{5}" \
                .format(find_info[0][0], find_info[0][1], find_info[0][2], find_info[0][3], find_info[0][4], find_info[0][5])
            mb.showinfo(":: Інформація про фільм ::", info)

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

    # функція відкриття вікна "Друк списку"
    def print_list(self):
        # Відкриття файлу виводу reslist.html
        try:
            fout = open('reslist.html', 'wt')
        except:
            mb.showerror('Помилка', 'Неможливо створити файл виводу!!!')
            return
        print('<html><head><title>Список елементів</title></head><body>', file=fout)
        print('<table border = "1" cellpadding="5">', file=fout)
        print(
            '<tr bgcolor="yellow"><td>Назва фільму</td><td>Країна</td><td>Жанр</td><td>Рік</td><td>Режисер</td><td>Оскар</td></tr>',
            file=fout)

        df = pd.read_csv('movie5.csv', sep=';', header=0)
        df = df.sort_values(by='name', ascending=True)

        for select in df.values.tolist():
            print('<tr>', file=fout)
            print('<td>{}</td>'.format(select[0]), file=fout)
            print('<td>{}</td>'.format(select[1]), file=fout)
            print('<td>{}</td>'.format(select[2]), file=fout)
            print('<td>{}</td>'.format(select[3]), file=fout)
            print('<td>{}</td>'.format(select[4]), file=fout)
            print('<td>{}</td>'.format(select[5]), file=fout)
            print('</tr>', file=fout)
        print('</table></body></html>', file=fout)
        fout.close()
        os.startfile("reslist.html")

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