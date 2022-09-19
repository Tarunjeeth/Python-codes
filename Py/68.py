from tkinter import *
from tkinter import ttk

def add ():
    l.append(n1.get())
    cb.configure(values=l)
    n1.delete(0,END)
    n1.focus()
    f=open("combo.txt",mode='w')
    for i in cb["values"]:
        f.write("\n"+i)
    """f.writelines(l)"""
    f.close()

def textcombo ():
    global l
    f=open("combo.txt",mode='r')
    txt=f.read()
    t=txt.split("\n")
    l=[]
    for i in t:
        if (i):
            l.append(i)
    cb["values"]=tuple(t)
    f.close()

root=Tk()
n1=Entry(root,width=30)
n1.pack()
cb=ttk.Combobox(root)
cb.pack()
btn=Button(root,text="add",command=add)
btn.pack()
textcombo()
root.mainloop()
