from __future__ import unicode_literals
from youtubedl import youtube_dl
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

    if d['status'] == 'downloading':
        print('Now downloading {}  :: eta {} :: speed {}'.format(d["filename"], d["eta"], d["speed"]))


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    "listformats" : lambda : print("list")
}
"""with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/Fp2LNyMssCA'])"""

# The Application GUI
root = Tk()

# tkinter variables
file_but_img = PhotoImage(file="icons/thumb__ownloads_folder.gif").subsample(10, 10)
restart_but_img = ImageTk.PhotoImage(Image.open("icons/reload_32px.png"))
play_but_img = ImageTk.PhotoImage(Image.open("icons/play_arrow_32px.png"))
stop_but_img = ImageTk.PhotoImage(Image.open("icons/stop_32px.png"))
delete_but_img = ImageTk.PhotoImage(Image.open("icons/delete_32px.png"))
move_down_dut_img = ImageTk.PhotoImage(Image.open("icons/arrow_down_32px.png"))
move_up_but_img = ImageTk.PhotoImage(Image.open("icons/arrow_up_32px.png"))
download_but_img = ImageTk.PhotoImage(Image.open("icons/cloud_download_32px.png"))

status_var = StringVar()
status_var.set("Welcome..")
tkvar = StringVar(root)
choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
tkvar.set('Pizza')

canvas1 = Frame(root, bg='white', width=775, height=226)
canvas1.grid(sticky="WE")
canvas2 = Canvas(root, bg='red', width=775, height=94)
canvas2.grid(sticky="WE")
canvas3 = Canvas(root, bg='white', width=775, height=200)
canvas3.grid(sticky="WE")
canvas4 = Canvas(root, bg='white', width=775, height=56)
canvas4.grid(sticky="WE")
status_bar = Canvas(root, bg="grey", width=775, height=37)
status_bar.grid(sticky="WE")

# Actual widgets

# the menu-bar
menubar = Menu(root, tearoff=0)
# file-menu
filemenu = Menu(tearoff=0)
filemenu.add_command(label="Exit", command=lambda: root.destroy(), font=("Courier", 10))
# menu-bar config
menubar.add_cascade(label="File", menu=filemenu)

# url entry text widget
enter_urllb = Label(canvas1, text=" Enter URLs Below : ", bg="white")
enter_urllb.grid(sticky=W, row=1, column=1, pady=4, padx=5)
urls_text = Text(canvas1, width=76, height=10, font=("Courier", 12), wrap='none', relief=GROOVE, bd=3)
urls_text.grid(row=2, column=1, padx=5)

# serach folder button
file_but = Button(canvas2, image=file_but_img)
file_but.grid(row=1, column=1, padx=15, pady=5)
# downloads folder combobox
down_path_lb = Label(canvas2, text="Download Folder :", font=("Courier", 10))
down_path_lb.grid(row=1, column=2, sticky="W")
down_path_combo = ttk.Combobox(canvas2, width=20, font=("Courier", 12))
down_path_combo.grid(row=1, column=3, padx=1)
# formats option menu
option_canv = Canvas(canvas2, bg="red", bd=0)
option_canv.grid(row=1, column=5, padx=30, sticky=W)
popupMenu = OptionMenu(option_canv, tkvar, *choices)
Label(option_canv, text="Format:").grid(row=1, column=1)
popupMenu.grid(row=1, column=2, padx=5)
# add button
add_but = Button(option_canv, text="ADD", padx=10, pady=5)
add_but.grid(row=1, column=3, padx=70, pady=4)
# download list label
download_list_lb = Label(canvas2, text="Download List: ", font=("Courier", 12))
download_list_lb.grid(row=2, column=1, columnspan=2, sticky=W)

# download list table
treeview = ttk.Treeview(canvas3, height=12)
treeview.config(columns=('fm', 'si', 'pr', 'sp', 'et', 'st'))
treeview.column('#0', minwidth=200, anchor=CENTER, width=200)
treeview.column('fm', minwidth=90, anchor=CENTER, width=90)
treeview.column('si', minwidth=80, anchor=CENTER, width=80)
treeview.column('pr', minwidth=130, anchor=CENTER, width=130)
treeview.column('sp', minwidth=100, anchor=CENTER, width=100)
treeview.column('et', minwidth=60, anchor=CENTER, width=60)
treeview.column('st', minwidth=120, anchor=CENTER, width=120)
treeview.heading('#0', text='Name')
treeview.heading('fm', text='Format')
treeview.heading('si', text='Size')
treeview.heading('pr', text='Progress')
treeview.heading('sp', text='Speed')
treeview.heading('et', text='ETA')
treeview.heading('st', text='Status')
treeview.grid(row=1, column=1, sticky="EW")

# restart download button
restart_but = Button(canvas4, image=restart_but_img)
restart_but.grid(row=1, column=1, padx=5, pady=7)
# play preview button
play_but = Button(canvas4, image=play_but_img)
play_but.grid(row=1, column=2, padx=5, pady=7)
# stop download button
stop_but = Button(canvas4, image=stop_but_img)
stop_but.grid(row=1, column=3, padx=5, pady=7)
# delete download button
delete_but = Button(canvas4, image=delete_but_img)
delete_but.grid(row=1, column=4, padx=5, pady=7)
# move selected down
move_down_dut = Button(canvas4, image=move_down_dut_img)
move_down_dut.grid(row=1, column=5, padx=5, pady=7)
# move selected up
move_up_but = Button(canvas4, image=move_up_but_img)
move_up_but.grid(row=1, column=6, padx=5, pady=7)
# download button
Label(canvas4, bg="white", width=60).grid(row=1, column=7)
download_but = Button(canvas4, image=download_but_img)
download_but.grid(row=1, column=8, sticky="E")

# Status bar
status = Label(status_bar, textvariable=status_var, bg="grey")
status.grid(row=1, column=1, sticky="W", padx=10, pady=10)

root.geometry("782x642")
# root.resizable(width=False, height=False)
root.title("YouTube-Downloader")
root.config(menu=menubar)
root.mainloop()

