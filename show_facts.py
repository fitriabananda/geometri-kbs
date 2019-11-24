import tkinter
from tkinter import *
from tkinter import scrolledtext, Menu, filedialog, messagebox

root = tkinter.Tk(className="Show Facts")
textPad = scrolledtext.ScrolledText(root, width=100, height=80)

def open():
    file = open("D:/geometri-kbs/data/facts.clp").read()
    if file != None:
        textPad.insert('1.0',file)

def exit():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
open()
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=exit)

textPad.pack()
root.mainloop()