from tkinter import *

def justify ():
      if (labl['justify']=='center'):
            labl.configure(justify='right')
      elif (labl['justify']=='right'):
            labl.configure(justify='left')
      elif (labl['justify']=='left'):
            labl.configure(justify='center')
def stick ():
      if (s.get()=='ew'):
            s.set('n')
      elif(s.get()=='n'):
            s.set('ne')
      elif(s.get()=='ne'):
            s.set('e')
      elif(s.get()=='e'):
            s.set('se')
      elif(s.get()=='se'):
            s.set('s')
      elif(s.get()=='s'):
            s.set('sw')
      elif(s.get()=='sw'):
            s.set('w')
      elif(s.get()=='w'):
            s.set('nw')
      elif(s.get()=='nw'):
            s.set('ew')
      labl.grid(stick=s.get())
      
win=Tk()
win.geometry("1200x1200")
s=StringVar()
s.set('ew')
labl=Label(win,text="Hello,Hello,Hello,Hello,Hello!!\nhi,hi,hi,hi,hi,hi!!\nworld,world,world,world,world,world!!!")
labl.grid(row=0,column=0)
but=Button(win,text="Justify",command=justify)
but.grid(row=2,column=0)
but1=Button(win,text="stick",command=stick)
but1.grid(row=2,column=1)
labl1=Label(win,height=30,text="Qwerty")
labl1.grid(row=0,column=1)
labl2=Label(win,width=100,text="Qwerty2")
labl2.grid(row=3,column=0)
