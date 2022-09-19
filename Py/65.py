from tkinter import *

def changestate ():
    btn4['state']=s.get()
    btn4.configure(text=s.get())

win=Tk()
s=StringVar()
s.set("active")
btn1=Radiobutton(win,text="disabled",value="disabled",variable=s)
btn1.grid(row=0,column=0)
btn2=Radiobutton(win,text="active",value="active",variable=s)
btn2.grid(row=1,column=0)
btn3=Button(win,text="change",command=changestate)
btn3.grid(row=2,column=0)
btn4=Button(win,text="active")
btn4.grid(row=3,column=0)
