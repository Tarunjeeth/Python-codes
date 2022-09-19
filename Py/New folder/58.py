from tkinter import *
from tkinter import ttk

def output ():
      nam=n1.get()
      gen=s.get()
      sta=cb.get()
      l=[nam,gen,sta]
      view.insert("",'end',values=l)


win=Tk()
win.geometry("720x1080")
labl=Label(win,text="Name:",font="77")
labl.grid(row=1,column=0)
n1=Entry(win,width=35)
n1.grid(row=1,column=1)
labl1=Label(win,text="Gender:",font="77")
labl1.grid(row=2,column=0)
s=StringVar()
s.set("Male")
r1=Radiobutton(win,text="Male",value="Male",variable=s)
r1.grid(row=2,column=1)
r2=Radiobutton(win,text="female",value="female",variable=s)
r2.grid(row=2,column=2)
labl2=Label(win,text="State")
labl2.grid(row=3,column=0)
cb=ttk.Combobox(win,value=["Tamilnadu","Puducherry","AndhraPradesh"])
cb.grid(row=3,column=1)
cb.current(0)
but=Button(win,text="output",command=output)
but.grid(row=4,column=0)
view=ttk.Treeview(win,columns=("c1","c2","c3"),show="headings")
view.grid(row=5,column=0)
view.heading("#1",text="Name")
view.heading("#2",text="Gender")
view.heading("#3",text="State")

