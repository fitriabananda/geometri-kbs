import tkinter
from tkinter import *
from tkinter import scrolledtext, Menu, filedialog, messagebox

root = tkinter.Tk(className="Show Rules")
textPad = scrolledtext.ScrolledText(root, width=100, height=80)

def open_command():
    file = open("D:/Documents/Akademik/Teknik Informatika/Semester 5/Inteligensi Buatan/Tugas/Tubes 2/geometri-kbs/rules.txt").read()
    if file != None:
        textPad.insert('1.0',file)

def exit_command():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
open_command()
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=exit_command)

textPad.pack()
root.mainloop()