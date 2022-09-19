from tkinter import *
from tkinter import ttk
from tkinter import messagebox

dict={"pen":"It is used for writing","pc":"Personal Computer","RAM":"Random access memory","SSD":"Solid state Drive"}
def descr ():
      shrtfr=cb.get()
      for i in dict:
            if(i==shrtfr):
                  labl.configure(text=dict[i])
                  break
            
root=Tk()
cb=ttk.Combobox(root,value=["pen","pc","RAM","SSD"])
cb.grid(row=1,column=0)
labl=Label(root)
labl.grid(row=2,column=0)
button=Button(root,text="Info",command=descr)
button.grid(row=3,column=0)
