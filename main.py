import os 
import img_processing as proc
import shape_rules as shape
from tkinter import *
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import filedialog, scrolledtext
from PIL import ImageTk,Image  

def open_image():
    file = filedialog.askopenfilename()
    loadclp = shape.Shape()
    countLine, savedlines, lineLength, countDegree, angleDegree, angleCross, angleFacing, countLineParallel = proc.process(file)
    jumlahsisi = "jumlahsisi " + str(countLine)
    loadclp.add_fact(jumlahsisi)
    panjangsisi = "panjangsisi "
    for sisi in lineLength:
        panjangsisi = panjangsisi + str(sisi) + " "
    loadclp.add_fact(panjangsisi)
    besarsudut = "besarsudut "
    for sudut in angleDegree:
        besarsudut = besarsudut + str(sudut[2]) + " "
    loadclp.add_fact(besarsudut)
    

    canvas = Canvas(window, bg="white", height=400) 
    canvas.grid(row=1, column=0, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N) 
    img = ImageTk.PhotoImage(Image.open(file))    
    canvas.create_image(20,20, anchor=NW, image=img)    
    canvas.image = img
    show_image_result(os.path.basename(file))
    loadclp.run_clp()
    show_matched_facts(loadclp)
    show_hit_rules()

def show_image_result(file):
    outfile = "./img/out" + file
    canvas = Canvas(window, bg="white", height=400) 
    canvas.grid(row=1, column=4, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N)
    img = ImageTk.PhotoImage(Image.open(outfile))    
    canvas.create_image(20,20, anchor=NW, image=img)    
    canvas.image = img
    show_result(outfile)
    print(outfile)

def show_result(outfile):
    canvas1 = Canvas(window, bg="white") 
    canvas1.grid(row=4, column=0, columnspan=2, padx=5, sticky=E+W+S+N)
    if outfile != None:    
        canvas1.create_text(50,20,fill="green",font="40",text="BERHASIL")
    else:
        canvas1.create_text(50,20,text="GAGAL")
    lbl.grid(row=4,column=0)

def show_matched_facts(loadclp):
    canvas4 = Canvas(window) 
    canvas4.grid(row=4, column=3, columnspan=2, padx=5, sticky=E+W+S+N)
    textPad = scrolledtext.ScrolledText(window, height=16, width=45)
    print(loadclp.py_pfact())
    file = open("data/matched_facts.txt", "w+")
    for f in loadclp.py_pfact():
        file.write(str(f) + "\n")
    file.close()
    file = open("data/matched_facts.txt").read()
    # file = open("data/shape_rules.clp").read()
    if file != None:
        textPad.insert('1.0',file)
    canvas4.create_window(193,135,window=textPad)

def show_hit_rules():
    canvas5 = Canvas(window, bg="white") 
    canvas5.grid(row=4, column=6, columnspan=2, padx=5, sticky=E+W+S+N)
    textPad = scrolledtext.ScrolledText(window, height=16, width=45)
    file = open("data/shape_rules.clp").read()
    if file != None:
        textPad.insert('1.0',file)
    canvas5.create_window(193,135,window=textPad)

def rule_editor():
    os.system('python ./rule_editor.py')

def show_rules():
    os.system('python ./show_rules.py')

def show_facts():
    os.system('python ./show_facts.py')

window = Tk()
window.attributes("-fullscreen", True)
    
window.title("Windows")

lbl = Label(window, text="Source Image")
lbl.grid(sticky=W, row=0, column=0, pady=4, padx=5)
canvas = Canvas(window, bg="white", height=400) 
canvas.grid(row=1, column=0, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N)

lbl2 = Label(window, text="Detection Image")
lbl2.grid(sticky=W, row=0, column=4, pady=4, padx=5)
canvas2 = Canvas(window, bg="white", height=400) 
canvas2.grid(row=1, column=4, columnspan=4, rowspan=2, padx=5, sticky=E+W+S+N)

lbl3 = Label(window, text="Detection Result")
lbl3.grid(sticky=W, row=3, column=0, pady=4, padx=5)
canvas3 = Canvas(window, bg="white") 
canvas3.grid(row=4, column=0, columnspan=2, padx=5, sticky=E+W+S+N)

lbl4 = Label(window, text="Matched Fact")
lbl4.grid(sticky=W, row=3, column=3, pady=4, padx=5)
canvas4 = Canvas(window, bg="white") 
canvas4.grid(row=4, column=3, columnspan=2, padx=5, sticky=E+W+S+N)

lbl5 = Label(window, text="Hit Rules")
lbl5.grid(sticky=W, row=3, column=6, pady=4, padx=5)
canvas5 = Canvas(window, bg="white") 
canvas5.grid(row=4, column=6, columnspan=2, padx=5, sticky=E+W+S+N)

abtn = Button(window, text="Open Image", width=20, command=open_image)
abtn.place(x=1180,y=30)

bbtn = Button(window, text="Open Rule Editor", width=20, command=rule_editor)
bbtn.place(x=1180,y=70)

cbtn = Button(window, text="Show Rules", width=20, command=show_rules)
cbtn.place(x=1180,y=110)

dbtn = Button(window, text="Show Facts", width=20, command=show_facts)
dbtn.place(x=1180,y=150) 

window.mainloop()