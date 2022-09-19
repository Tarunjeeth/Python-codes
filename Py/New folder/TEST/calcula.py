from tkinter import *

def click(number):
    global opt
    opt=opt+str(number)
    inp.set(opt)

def clear():
    global opt
    opt=""
    inp.set(opt)

def equal():
    global opt
    result=eval(opt)
    inp.set(result)
    opt=""



win=Tk()
win.title("Calculator")
win.resizable(width=False,height=False)
inp=StringVar()
opt=""
disp=Entry(win,font=("ariel",20,"bold"),textvariable=inp,bd=10,justify="right",state="disabled",disabledbackground="darkgrey",disabledforeground="black").grid(columnspan=4)
btn7=Button(win,text="7",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click("7")).grid(column=0,row=1)
btn8=Button(win,text="8",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(8)).grid(column=1,row=1)
btn9=Button(win,text="9",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(9)).grid(column=2,row=1)
btndiv=Button(win,text="/",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click("/")).grid(column=3,row=1)
btn4=Button(win,text="4",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(4)).grid(column=0,row=2)
btn5=Button(win,text="5",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(5)).grid(column=1,row=2)
btn6=Button(win,text="6",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(6)).grid(column=2,row=2)
btnmul=Button(win,text="*",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click("*")).grid(column=3,row=2)
btn1=Button(win,text="1",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(1)).grid(column=0,row=3)
btn2=Button(win,text="2",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(2)).grid(column=1,row=3)
btn3=Button(win,text="3",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(3)).grid(column=2,row=3)
btnsub=Button(win,text="-",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click("-")).grid(column=3,row=3)
btnclear=Button(win,text="c",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=clear).grid(column=0,row=4)
btn0=Button(win,text="0",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click(0)).grid(column=1,row=4)
btneq=Button(win,text="=",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=equal).grid(column=2,row=4)
btnadd=Button(win,text="+",padx=10,bd="5",fg="black",font=("ariel",20,"bold"),command=lambda:click("+")).grid(column=3,row=4)
