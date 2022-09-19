from tkinter import *
root=Tk()
root.title("Hello world")
root.geometry("600x800")
root.configure(bg="cyan")
msg=Label(root,text="welcome!",bg="magenta",fg="yellow",font="32")
msg.grid(row=0,column=1,padx=200)
root.mainloop()
