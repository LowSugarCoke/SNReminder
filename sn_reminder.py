import sn_lib
import sn_reminder_manager
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.createWidgets()

    def createWidgets(self):
        self.geometry('800x500')
        self.entry_collect_anime = tk.Entry(
            self, width=35, font=('Arial 24')).grid(row=0, column=0, padx=20, pady=20)
        self.button_collect = tk.Button(self, height=2, text='收藏動漫', command=self.connect_collect_button).grid(
            row=0, column=1, padx=20, pady=20)

        self.listbox = tk.Listbox(self, width=70, height=20, font=('Arial 12'))
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

    def connect_update_button(self):
        print("連接更新動漫")

    def connect_collect_list_button(self):
        print("連接收藏動漫更新")


if __name__ == '__main__':
    # SNLib = sn_lib.SNLib()
    # if SNLib.crawl_sn_web() == False:
    #     print("Something wrong")
    # SNLib.read_anime()

    # while 1:
    #     print("請輸入下列指令")
    #     try:
    #         command = int(input("1. 收藏動漫\n2. 顯示更新動漫列表\n3. 收藏動漫列表\n"))
    #     except:
    #         print("輸入錯誤，請再次輸入")
    #         continue
    #     if not(command > 0 and command <= 3):
    #         print("輸入錯誤，請再次輸入")
    #         continue

    #     if command == 1:py
    #         SNLib.collect_anime()
    #         SNLib.read_anime()
    #     if command == 2:
    #         SNLib.print_update_anime_web()
    #     if command == 3:
    #         is_update = SNLib.check_anime_update()
    #         if(is_update):
    #             SNLib.write_anime_update()
    #             SNLib.read_anime()
    #         SNLib.print_local_anime()

    app = Application()
    app.title("SN Reminder")
    app.mainloop()
