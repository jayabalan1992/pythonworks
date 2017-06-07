import os
from tkinter import *
root = Tk()
label1=Label(root,text="Host Address")
label1.grid(row=0,sticky=E)
v = StringVar()
c= StringVar()

entry1=Entry(root, textvariable=v)
entry1.grid(row=0,column=1)

label2=Label(root,text="count")
label2.grid(row=1,sticky=E)
entry2=Entry(root,textvariable=c)
entry2.grid(row=1,column=1)


v.set("localhost")
c.set(4)

def test():
    s = v.get()
    os.system("ping "+s+" -n "+str(c.get()))

button1=Button(root,text="Click me",command=test)
button1.grid(columnspan=2)


root.mainloop()