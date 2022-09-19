from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


des=sqlite3.connect("salary.db")
c=des.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS SAL (empno int,empname text,salary float)""")
des.commit()
des.close()

def insert ():
      des=sqlite3.connect("salary.db")
      c=des.cursor()
      s=n1.get()
      c.execute("SELECT * FROM SAL WHERE empno='"+s+"'")
      tab=c.fetchall()
      if (tab):
            messagebox.showerror("Error","Already exists")
      else:
            if (n1.get()=="" or n2.get()=="" or n3.get()==""):
                  messagebox.showerror("Error","Enter the data first")
            else:
                  c.execute("INSERT INTO SAL VALUES (:empno,:empname,:salary)",{'empno':n1.get(),'empname':n2.get(),'salary':n3.get()})
                  messagebox.showinfo("Info","inserted succesfully")
                  n1.delete(0,END)
                  n2.delete(0,END)
                  n3.delete(0,END)
      des.commit()
      des.close()
      view()
      
def search ():
      des=sqlite3.connect("salary.db")
      c=des.cursor()
      s=n1.get()
      c.execute("SELECT * FROM SAL WHERE empno='"+s+"'")
      tab=c.fetchall()
      n2.delete(0,END)
      n3.delete(0,END)
      if (not tab):
            messagebox.showerror("Error","Not found")
      else:
           n2.insert(END,str(tab[0][1]))
           n3.insert(END,str(tab[0][2]))
      des.commit()
      des.close()

def update ():
      des=sqlite3.connect("salary.db")
      c=des.cursor()
      s=n1.get()
      c.execute("SELECT * FROM SAL WHERE empno='"+s+"'")
      tab=c.fetchall()
      if (not tab):
            messagebox.showerror("Error","not found")
      else:
            c.execute('''UPDATE SAL set empno=:r,empname=:n,salary=:b WHERE empno=:r''',{'r':s,'n':n2.get(),'b':n3.get()})
            messagebox.showinfo("info","Updated succesfully")
      n1.delete(0,END)
      n2.delete(0,END)
      n3.delete(0,END)
      des.commit()
      des.close()
      view()

def delete ():
      des=sqlite3.connect("salary.db")
      c=des.cursor()
      s=n1.get()
      c.execute("SELECT * FROM SAL WHERE empno='"+s+"'")
      tab=c.fetchall()
      if (not tab):
            messagebox.showerror("Error","not found")
      else:
            msg=messagebox.askquestion("Delete","Are you sure to delete??")
            if(msg=="yes"):
                  c.execute("DELETE FROM SAL WHERE empno='"+s+"'")
                  messagebox.showinfo("Info","Deleted sucessfully")
                  n1.delete(0,END)
                  n2.delete(0,END)
                  n3.delete(0,END)
      des.commit()
      des.close()
      view()

def view ():
      des=sqlite3.connect("salary.db")
      c=des.cursor()
      c.execute("SELECT * FROM SAL")
      tab=c.fetchall()
      for row in viewtrv.get_children():
            viewtrv.delete(row)
      k=0
      for s in tab:
            l=[]
            l.append(tab[k][0])
            l.append(tab[k][1])
            b=tab[k][2]
            d=int(b*0.2)
            g=int(b)+d
            t=int(g*0.10)
            n=g-t
            l.append(b)
            l.append(d)
            l.append(t)
            l.append(n)
            viewtrv.insert("",END,values=l)
            k=k+1
      des.commit()
      des.close()
            
win=Tk()
labl=Label(win,text="employee number")
labl.grid(row=0,column=0)
n1=Entry(win,width=40)
n1.grid(row=0,column=1)
labl1=Label(win,text="employee name")
labl1.grid(row=1,column=0)
n2=Entry(win,width=40)
n2.grid(row=1,column=1)
labl2=Label(win,text="employee salary")
labl2.grid(row=2,column=0)
n3=Entry(win,width=40)
n3.grid(row=2,column=1)
but=Button(win,text="insert",command=insert)
but.grid(row=3,column=0)
but1=Button(win,text="view",command=view)
but1.grid(row=3,column=1)
but2=Button(win,text="search",command=search)
but2.grid(row=3,column=2)
but3=Button(win,text="update",command=update)
but3.grid(row=3,column=3)
but4=Button(win,text="delete",command=delete)
but4.grid(row=3,column=4)
viewtrv=ttk.Treeview(win,columns=("c1","c2","c3","c4","c5","c6"),show="headings")
viewtrv.grid(row=4,column=0,columnspan=5)
viewtrv.heading("#1",text="employee no.")
viewtrv.heading("#2",text="employee name")
viewtrv.heading("#3",text="basic salary")
viewtrv.heading("#4",text="da")
viewtrv.heading("#5",text="tds")
viewtrv.heading("#6",text="net salary")


