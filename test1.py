from Tkinter import *
import Tkinter

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="circle")
B2 = Tkinter.Button(top, text ="vidhya", relief=RAISED,\
                         cursor="target")
B1.pack()
B2.pack()
top.mainloop()