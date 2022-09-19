from tkinter import *

def name ():
    labl2.configure(text="Welcome"+ent.get())

root=Tk()
root.geometry("1920x1080")
root.title("Testbench")
root.configure(bg="magenta")
lab1=Label(root,text="Enter your name",font="99")
lab2=Label(root)
ent=Entry(root,text="Enter your name",font="66")
button=Button(root,text="START",font="66",command=name)\
root.mainloop()

