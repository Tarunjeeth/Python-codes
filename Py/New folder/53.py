from tkinter import *

def addition ():
      num1=n1.get()
      num2=n2.get()
      if(num1!="" and num2!=""):
            result=int(num1)+int(num2)
            labl3.configure(text=str(result))
def subtraction ():
      num1=int(n1.get())
      num2=int(n2.get())
      if(num1!="" and num2!=""):
            result=int(num1)-int(num2)
            labl3.configure(text=str(result))
def multiplication ():
      num1=int(n1.get())
      num2=int(n2.get())
      if(num1!="" and num2!=""):
            result=int(num1)*int(num2)
            labl3.configure(text=str(result))
def division ():
      num1=int(n1.get())
      num2=int(n2.get())
      if(num1!="" and num2!=""):
            result=int(num1)/int(num2)
            labl3.configure(text=str(result))
      
win=Tk()
win.title("geo_calc")
win.geometry("720x1080")
win.configure(bg="grey")
labl1=Label(win,text="enter a number",bg="white",font="88")
labl1.grid(row=0,column=0)
n1=Entry(win,width=30)
n1.grid(row=0,column=1)
labl2=Label(win,text="enter another number",bg="white",font="88")
labl2.grid(row=1,column=0)
n2=Entry(win,width=30)
n2.grid(row=1,column=1)
labl3=Label(win)
labl3.grid(row=2,column=0)
but1=Button(win,text="add",command=addition)
but1.grid(row=3,column=0)
but2=Button(win,text="multiply",command=multiplication)
but2.grid(row=3,column=1)
but3=Button(win,text="subtract",command=subtraction)
but3.grid(row=3,column=2)
but4=Button(win,text="divide",command=division)
but4.grid(row=3,column=3,)

