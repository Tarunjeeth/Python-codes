from tkinter import *
win=Tk()
win.geometry("720x1080")
s=StringVar()
s.set("Orange")
r1=Radiobutton(win,text="Apple",value="Apple",variable=s)
r1.grid(row=0,column=1)
r2=Radiobutton(win,text="Orange",value="Orange",variable=s)
r2.grid(row=0,column=2)
labl=Label(win,textvariable=s)
labl.grid(row=1,column=0)
