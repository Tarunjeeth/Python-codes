from pathlib import Path
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Tarunjeeth\Music\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

mrksht=sqlite3.connect("marks.db")
c=mrksht.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS MARK (roll int,name text,maths float,science float,social float)""")
mrksht.commit()
mrksht.close()

def insert():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      if (tab):
            messagebox.showerror("Error","Already exists")
      else:
            if (n1.get()=="" or n2.get()=="" or n3.get()=="" or n4.get()=="" or n5.get()==""):
                  messagebox.showerror("Error","Enter the data first")
            if (int(n3.get())>100 or int(n4.get())>100 or int(n5.get())>100):
                  messagebox.showerror("Error","mark exeeds 100-limit")
            else:
                  c.execute("INSERT INTO MARK VALUES (:roll,:name,:maths,:science,:social)",{'roll':n1.get(),'name':n2.get(),'maths':n3.get(),'science':n4.get(),'social':n5.get()})
                  messagebox.showinfo("Info","inserted succesfully")
                  n1.delete(0,END)
                  n2.delete(0,END)
                  n3.delete(0,END)
                  n4.delete(0,END)
                  n5.delete(0,END)
      mrksht.commit()
      mrksht.close()
      view()

def search ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      n2.delete(0,END)
      n3.delete(0,END)
      n4.delete(0,END)
      n5.delete(0,END)
      if (not tab):
            messagebox.showerror("Error","Not found")
      else:
           n2.insert(END,str(tab[0][1]))
           n3.insert(END,str(tab[0][2]))
           n4.insert(END,str(tab[0][3]))
           n5.insert(END,str(tab[0][4]))
      mrksht.commit()
      mrksht.close()

def update ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      if (not tab):
            messagebox.showerror("Error","not found")
      else:
            c.execute('''UPDATE MARK set roll=:q,name=:r,maths=:n,science=:b,social=:v WHERE roll=:q''',{'q':s,'r':n2.get(),'n':n3.get(),'b':n4.get(),'v':n5.get()})
            messagebox.showinfo("info","Updated succesfully")
      n1.delete(0,END)
      n2.delete(0,END)
      n3.delete(0,END)
      n4.delete(0,END)
      n5.delete(0,END)
      mrksht.commit()
      mrksht.close()
      view()

def delete ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      s=n1.get()
      c.execute("SELECT * FROM MARK WHERE roll='"+s+"'")
      tab=c.fetchall()
      if (not tab):
            messagebox.showerror("Error","not found")
      else:
            msg=messagebox.askquestion("Delete","Are you sure to delete??")
            if(msg=="yes"):
                  c.execute("DELETE FROM MARK WHERE roll='"+s+"'")
                  messagebox.showinfo("Info","Deleted sucessfully")
                  n1.delete(0,END)
                  n2.delete(0,END)
                  n3.delete(0,END)
                  n4.delete(0,END)
                  n5.delete(0,END)
      mrksht.commit()
      mrksht.close()
      view()

def view ():
      mrksht=sqlite3.connect("marks.db")
      c=mrksht.cursor()
      c.execute("SELECT * FROM MARK")
      tab=c.fetchall()
      for row in viewtrv.get_children():
            viewtrv.delete(row)
      k=0
      for s in tab:
            l=[]
            l.append(tab[k][0])
            l.append(tab[k][1])
            m=tab[k][2]
            s=tab[k][3]
            ss=tab[k][4]
            tm=int(s+ss+m)
            av=int(tm/3)
            if (av>=90):
                  grade="A"
            elif (av>=70):
                  grade="B"
            elif (av>=40):
                  grade="C"
            else:
                  grade="D"
            l.append(m)
            l.append(s)
            l.append(ss)
            l.append(tm)
            l.append(grade)
            viewtrv.insert("",END,values=l)
            k=k+1
      mrksht.commit()
      mrksht.close()
      



window = Tk()

window.geometry("1405x548")
window.configure(bg = "#FFFFFF")


canvas = Canvas(window,bg = "#fbf7ad",height = 548,width = 1410,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)


canvas.create_text(41.0,20.0,anchor="nw",text="Roll no",fill="#000000",font=("Inter ExtraBold", 12 * -1))

canvas.create_text(41.0,52.0,anchor="nw",text="Name",fill="#000000",font=("Inter ExtraBold", 12 * -1))

canvas.create_text(36.0,84.0,anchor="nw",text="Maths Mark",fill="#000000",font=("Inter ExtraBold", 12 * -1))

canvas.create_text(31.0,148.0,anchor="nw",text="Chemistry Mark",fill="#000000",font=("Inter ExtraBold", 12 * -1))

canvas.create_text(34.0,116.0,anchor="nw",text="Physics Mark",fill="#000000",font=("Inter ExtraBold", 12 * -1))

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(1000.0,90.0,image=image_image_2)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(window,image=button_image_1,borderwidth=0,highlightthickness=0,command=delete,relief="flat")
button_1.place(x=424.0,y=194.0,width=76.00001525878906,height=24.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=search,relief="flat")
button_2.place(x=224.0,y=194.0,width=74.0,height=24.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=view,relief="flat")
button_3.place(x=124.0,y=194.0,width=74.0,height=24.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=insert,relief="flat")
button_4.place(x=31.0,y=194.0,width=74.0,height=24.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=update,relief="flat")
button_5.place(x=324.0,y=194.0,width=74.0,height=24.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(338.00000762939453,29.99999237060547,image=entry_image_1)
n1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
n1.place(x=163.9994888305664,y=19.991012573242188,width=348.00103759765625,height=18.017959594726562)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(338.0,62.0,image=entry_image_2)
n2= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
n2.place(x=164.0,y=52.0,width=348.0,height=18.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(338.0,94.0,image=entry_image_3)
n3= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
n3.place(x=164.0,y=84.0,width=348.0,height=18.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(338.0,126.0,image=entry_image_4)
n4= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
n4.place(x=164.0,y=116.0,width=348.0,height=18.0)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(338.0,158.0,image=entry_image_5)
n5= Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
n5.place(x=164.0,y=148.0,width=348.0,height=18.0)
viewtrv=ttk.Treeview(window,columns=("c1","c2","c3","c4","c5","c6","c7"),show="headings")
viewtrv.place(x=0,y=250)
viewtrv.heading("#1",text="roll no")
viewtrv.heading("#2",text="Student name")
viewtrv.heading("#3",text="Maths mark")
viewtrv.heading("#4",text="Science mark")
viewtrv.heading("#5",text="Social mark")
viewtrv.heading("#6",text="Total marks")
viewtrv.heading("#7",text="grade")
labltxt=Label(window,text="With 💖 ,Tarunjeeth PYTN-A1",bg="#fbf7ad",fg="#a50409",font="Times 10 bold")
labltxt.place(x=0,y=500)
window.resizable(False, False)
window.mainloop()
