from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

def calculator ():
      calcu=cb.get()
      num1=n1.get()
      num2=n2.get()
      if(num1!="" and num2!=""):
            if(calcu=="add"):
                  result=int(num1)+int(num2)
            elif(calcu=="multiply"):
                  result=int(num1)*int(num2)
            elif(calcu=="division"):
                  result=int(num1)/int(num2)
            elif(calcu=="subtraction"):
                  result=int(num1)-int(num2)
            else:
                  messagebox.showinfo("Select","please select a valid option")
            labl3.configure(text=str(result))
      else:
            messagebox.showinfo("enter","Please Enter numbers") 
win=Tk()
win.geometry("720x1080")
labl=Label(win,text="enter a number",font="88")
labl.grid(row=0,column=1)
n1=Entry(win,width=30)
n1.grid(row=0,column=2)
labl2=Label(win,text="enter another number",font="88")
labl2.grid(row=1,column=0)
n2=Entry(win,width=30)
n2.grid(row=1,column=1)
cb=ttk.Combobox(win,value=["select an option","add","multiply","division","subtraction"])
cb.grid(row=2,column=0)
cb.current(0)
labl3=Label(win)
labl3.grid(row=3,column=1)
button=Button(win,text="Calculate!",command=calculator)
button.grid(row=3,column=0)

