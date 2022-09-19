from tkinter import *

win=Tk()
file="IMG_0196.png"
img=PhotoImage(file=file)
file1="Untitled.png"
img1=PhotoImage(file=file1)
labl=Label(win,image=img)
labl.grid(row=0,column=0)
labl.image=img
labl2=Label(win,image=img1)
labl2.grid(row=1,column=0)
labl2.image=img1
