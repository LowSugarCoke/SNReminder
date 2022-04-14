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
        self.button_collect = tk.Button(self, height=2, text='收藏動漫').grid(
            row=0, column=1, padx=20, pady=20)

        self.listbox = tk.Listbox(self, width=70, height=20, font=('Arial 12'))
        for i in range(200):
            self.listbox.insert('end', i)
        self.listbox.grid(row=1, rowspan=3, column=0)

        self.button_update_list = tk.Button(self, height=2, text='更新動漫列表').grid(
            row=1, column=1, padx=20, sticky=tk.N)
        self.button_collect_list = tk.Button(self, height=2, text='收藏動漫列表').grid(
            row=1, column=1, padx=20, )

        self.checkbutton_reminder = tk.Checkbutton(
            self).grid(row=3, column=1, padx=20, sticky=(tk.W, tk.S))

        self.label_reminder = tk.Label(self, text="每日提醒").grid(
            row=3, column=1, padx=40, ipady=3, sticky=(tk.W, tk.S))
