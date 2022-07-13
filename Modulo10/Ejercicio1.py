import tkinter
from tkinter import ttk

w = tkinter.Tk()

w.columnconfigure(0,weight=1)
w.columnconfigure(0,weight=3)

b1= tkinter.StringVar()
b2= tkinter.StringVar()
r1= ttk.Radiobutton(w,text="opcion 1",value="1",variable=b1)
r2= ttk.Radiobutton(w,text="opcion 2",value="2",variable=b2)
r1.grid(column=0,row=0,padx=5,pady=5)
r2.grid(column=0,row=1,padx=5,pady=5)



w.mainloop()


label_nombres=tkinter.Label(w,text="Nombres")
label_nombres.pack()
