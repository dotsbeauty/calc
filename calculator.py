from tkinter import *
from functools import partial
win = Tk()
win.title("calc")
win.configure(bg="lightblue")
win.geometry('250x100')
def add(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    add = int(n1) + int(n2)
    label.config(text = "Result : %d" %add)
    return
    
def sub(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sub = int(n1) - int(n2)
    label.config(text = "Result : %d" %sub)
    return

def mul(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    mul = int(n1) * int(n2)
    label.config(text = "Result : %d" %mul)
    return
    
def div(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    div = float(n1) / int(n2)
    label.config(text = "Result : %f" %div)
    return

l1 = Label(win,text = "first no", background = "lightblue")
l1.grid(row = 1, column = 0)

l2 = Label(win,text = "second no", background = "lightblue")
l2.grid(row = 2, column = 0)

label = Label(win, background = "lightblue")
label.grid(row = 3, column = 7)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable = x1)
e1.grid(row = 1, column = 2)
e2 = Entry(win,textvariable = x2)
e2.grid(row = 2, column = 2)

add = partial(add, label,x1,x2)
button = Button(win, text = "+", command = add)
button.place(x = 0, y = 50)

sub = partial(sub, label,x1,x2)
button1 = Button(win, text = "-", command = sub)
button1.place(x = 30, y = 50)

mul = partial(mul, label,x1,x2)
button1 = Button(win, text = "*", command = mul)
button1.place(x = 60, y = 50)

div = partial(div, label,x1,x2)
button1 = Button(win, text = "/", command = div)
button1.place(x = 90, y = 50)

win.mainloop()