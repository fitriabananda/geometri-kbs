import tkinter
from tkinter import *
from tkinter import scrolledtext, Menu, filedialog, messagebox

root = tkinter.Tk(className="Rule Editor")
textPad = scrolledtext.ScrolledText(root, width=100, height=80)

def open():
    file = open("D:/geometri-kbs/data/rules.clp").read()
    if file != None:
        textPad.insert('1.0',file)

def save():
    f = open("D:/geometri-kbs/data/rules.clp", "w+")
    data = str(textPad.get('1.0', END))
    print(data)
    f.write(data)
    f.close()
    root.destroy()

def exit():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
open()
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

textPad.pack()
root.mainloop()