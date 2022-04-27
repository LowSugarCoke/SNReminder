"""
@author: Jack Lee
Reference: "https://sn-video.com/data/ajax/function/ajax_mainPage.php"

sn_reminder is a application to crawl the amine website and show the upating episodes on
the UI. It could save the anime in the local and update anime episodes through the 
crawling website.
"""
import sn_lib
import tkinter as tk


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
        self.var = tk.StringVar()
        self.entry_collect_anime = tk.Entry(
            self, textvariable=self.var, width=35, font=('Arial 24')).grid(row=0, column=0, padx=20, pady=20)
        self.button_collect = tk.Button(self, height=2, text='收藏動漫', command=self.connect_collect_button).grid(
            row=0, column=1, padx=20, pady=20)

        self.listbox = tk.Listbox(self, width=70, height=20, font=(
            'Arial 12'))
        self.listbox.grid(row=1, rowspan=3, column=0)

        self.button_update_list = tk.Button(self, height=2, text='更新動漫列表', command=self.connect_update_button).grid(
            row=1, column=1, padx=20, sticky=tk.N)
        self.button_collect_list = tk.Button(self, height=2, text='收藏動漫列表', command=self.connect_collect_list_button).grid(
            row=1, column=1, padx=20, )

    def connect_collect_button(self):
        print("連接收藏動漫")
        self.run(1)

    def connect_update_button(self):
        print("連接更新動漫")
        self.run(2)

    def connect_collect_list_button(self):
        print("連接收藏動漫更新")
        self.run(3)

    def show_listbox(self, anime_list):
        self.listbox.delete(0, tk.END)
        for anime in anime_list:
            self.listbox.insert(tk.END, anime+anime_list[anime])

    def show_listbox_local(self, local_anime):
        """ show local data on the listbox """

        self.listbox.delete(0, tk.END)
        for anime in local_anime:
            self.listbox.insert(
                tk.END, anime+local_anime[anime][0]+local_anime[anime][1])

    def run(self, command):
        if command == 1:
            text = self.var.get()
            if len(text) == 0:
                self.listbox.delete(0, tk.END)
                self.listbox.insert(0, "請輸入要收藏的動漫")
                return
            else:
                if self.SNLib.collect_anime(text):
                    self.SNLib.read_anime()
                    self.listbox.delete(0, tk.END)
                    self.listbox.insert(0, "成功收藏動漫")
                else:
                    self.listbox.delete(0, tk.END)
                    self.listbox.insert(0, "收藏動漫失敗")

        if command == 2:
            anime_list = self.SNLib.print_update_anime_web()
            self.show_listbox(anime_list)

        if command == 3:
            is_update = self.SNLib.check_anime_update()
            if(is_update):
                self.SNLib.write_anime_update()
                self.SNLib.read_anime()
            local_anime = self.SNLib.print_local_anime()
            self.show_listbox_local(local_anime)


if __name__ == '__main__':
    app = Application()
    app.title("SN Reminder")
    app.mainloop()
