from tkinter import *
from PIL import Image,ImageTk

win=Tk()
file="IMG_0129.jpg"
img=Image.open(file)
img1=ImageTk.PhotoImage(img)
lbl1=Label(win,image=img1)
lbl1.grid(row=0,column=0)
