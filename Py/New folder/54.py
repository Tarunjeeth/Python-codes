from tkinter import *

def name1():
      labl2.configure(text="welcome " + naent.get())

win=Tk()
win.title("welcome")
labl1=Label(win,text="enter your name",font="88")
labl1.grid(row=0,column=0)
naent=Entry(win,width=45)
naent.grid(row=0,column=1)
labl2=Label(win)
labl2.grid(row=1,column=0)
button=Button(win,text="press",command=name1)
button.grid(row=2,column=0)
win.mainloop()