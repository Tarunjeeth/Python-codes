from tkinter import *

def entry():
    s=n1.get()
    f=open("entry.txt",mode='w')
    f.write(s)
    f.close()

def open1():
    f=open("entry.txt",mode='r')
    txt=f.read()
    n1.insert(END,txt)
    f.close()
    
root=Tk()
n1=Entry(root,width=30)
n1.pack()
btn1=Button(root,text="open",command=open1)
btn1.pack()
btn=Button(root,text="save",command=entry)
btn.pack()

