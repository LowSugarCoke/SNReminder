import sn_lib
import tkinter as tk
from tkinter import ttk


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

    root = tk.Tk()
    root.geometry('800x500')
    entry_collect_anime = tk.Entry(
        root, width=35, font=('Arial 24')).grid(row=0, column=0, padx=20, pady=20)
    button_collect = tk.Button(root, height=2, text='收藏動漫').grid(
        row=0, column=1, padx=20, pady=20)

    listbox = tk.Listbox(root, width=70, height=20, font=('Arial 12'))
    for i in range(200):
        listbox.insert('end', i)
    listbox.grid(row=1, rowspan=3, column=0)

    button_update_list = tk.Button(root, height=2, text='更新動漫列表').grid(
        row=1, column=1, padx=20, sticky=tk.N)
    button_collect_list = tk.Button(root, height=2, text='收藏動漫列表').grid(
        row=1, column=1, padx=20, )

    checkbutton_reminder = tk.Checkbutton(
        root).grid(row=3, column=1, padx=20, sticky=(tk.W, tk.S))

    label_reminder = tk.Label(root, text="每日提醒").grid(
        row=3, column=1, padx=40, ipady=3, sticky=(tk.W, tk.S))
    root.mainloop()
