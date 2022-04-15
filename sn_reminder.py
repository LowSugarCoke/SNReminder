import sn_lib
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.SNLib = sn_lib.SNLib()
        if self.SNLib.crawl_sn_web() == False:
            print("Something wrong")
        self.SNLib.read_anime()

    def createWidgets(self):
        self.geometry('800x500')
        self.entry_collect_anime = tk.Entry(
            self, width=35, font=('Arial 24')).grid(row=0, column=0, padx=20, pady=20)
        self.button_collect = tk.Button(self, height=2, text='收藏動漫', command=self.connect_collect_button).grid(
            row=0, column=1, padx=20, pady=20)

        self.listbox = tk.Listbox(self, width=70, height=20, font=(
            'Arial 12'))
        for i in range(200):
            self.listbox.insert('end', i)
        self.listbox.grid(row=1, rowspan=3, column=0)

        self.button_update_list = tk.Button(self, height=2, text='更新動漫列表', command=self.connect_update_button).grid(
            row=1, column=1, padx=20, sticky=tk.N)
        self.button_collect_list = tk.Button(self, height=2, text='收藏動漫列表', command=self.connect_collect_list_button).grid(
            row=1, column=1, padx=20, )

        self.checkbutton_reminder = tk.Checkbutton(
            self).grid(row=3, column=1, padx=20, sticky=(tk.W, tk.S))

        self.label_reminder = tk.Label(self, text="每日提醒").grid(
            row=3, column=1, padx=40, ipady=3, sticky=(tk.W, tk.S))

    def connect_collect_button(self):
        print("連接收藏動漫")
        self.run(1)

    def connect_update_button(self):
        print("連接更新動漫")
        self.run(2)

    def connect_collect_list_button(self):
        print("連接收藏動漫更新")
        self.run(3)

    # def show_listbox(self,)

    def run(self, command):
        command = int(input("1. 輸入收藏動漫\t2. 線上更新清單\t3. 更新資料庫內容"))
        if command == 1:
            self.SNLib.collect_anime()
            self.SNLib.read_anime()
        if command == 2:
            self.SNLib.print_update_anime_web()
        if command == 3:
            is_update = self.SNLib.check_anime_update()
            if(is_update):
                self.SNLib.write_anime_update()
                self.SNLib.read_anime()
            self.SNLib.print_local_anime()


if __name__ == '__main__':
    app = Application()
    app.title("SN Reminder")
    app.mainloop()
