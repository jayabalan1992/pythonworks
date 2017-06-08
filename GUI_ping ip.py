import os
from tkinter import *
root = Tk()
label1=Label(root,text="Host Address",fg="blue")
label1.grid(row=0,sticky=E)
v = StringVar()
c= StringVar()
b=StringVar()
entry1=Entry(root, textvariable=v)
entry1.grid(row=0,column=1)
#Getting the count
label2=Label(root,text="count")
label2.grid(row=1,sticky=E)
entry2=Entry(root,textvariable=c)
entry2.grid(row=1,column=1)
#Getting the bytes
label2=Label(root,text="bytes",fg="green")
label2.grid(row=2,sticky=E)
entry2=Entry(root,textvariable=b)
entry2.grid(row=2,column=1)


label3=Label(root,text="developed by jay")
label3.grid(row=5,columnspan=4)

v.set("localhost")
c.set(4)
b.set(32)

def ping():
    s = v.get()
    print("="*40)
    print("Pinging "+s)
    os.system("ping "+s+" -n "+c.get()+" -l "+b.get())

def tracert():
    s=v.get()
    print("=" * 40)
    os.system("tracert "+s)

button1=Button(root,text="PING",command=ping,fg="red")
button1.grid(row=3,column=0)

button2=Button(root,text="Traceroute",command=tracert)
button2.grid(row=3,column=1)


root.mainloop()