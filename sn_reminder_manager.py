import sn_reminder_ui
import sn_lib
import tkinter as tk


class SNManager:
    def __init__(self):
        self.app = sn_reminder_ui.Application()
        self.app.title("SN Reminder")
        self.connect_ui()
        self.app.mainloop()
        # app = sn_reminder_ui.Application()
        # app.title("SN Reminder")
        # app.mainloop()

    def connect_ui(self):
        self.app.button_collect(command=self.connect_collect_button)
        self.app.button_update_list(command=self.connect_update_button)
        self.app.button_collect_list(command=self.connect_collect_list_button)

    def connect_collect_button(self):
        print("按下收藏動漫")

    def connect_update_button(self):
        print("按下更新按鈕")

    def connect_collect_list_button(self):
        print("按下收集清單")
