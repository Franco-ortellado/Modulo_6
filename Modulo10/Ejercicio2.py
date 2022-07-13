import tkinter
from tkinter import ttk

w = tkinter.Tk()

label_nombres=tkinter.Label(w,text="Nombres")
label_nombres.pack()

w.columnconfigure(0,weight=1)
w.columnconfigure(0,weight=3)

lista =["juan","pepe","Marcos"]
lista_items=tkinter.StringVar(value=lista)
lista_box = tkinter.Listbox(w, height=15, listvariable = lista_items)
lista_box.pack()



w.mainloop()