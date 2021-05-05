# calling gui tkinter
import tkinter as tk

# calling all tkinters functions
from tkinter import *

# parent window
root = tk.Tk()

# Code to add widgets will go here.

# giving the window a size
root.geometry("250x300")

# naming the window
root.title('Adding Numbers')

# naming variables
num1 = StringVar()
num2 = StringVar()
res = StringVar()

# naming labels in the
number1 = Label(root, text="First: ")
number2 = Label(root, text="Second: ")
Result = Label(root, text="Result: ")

# placing the labels
number1.place(x=10, y=10)
number2.place(x=10, y=35)
Result.place(x=10, y=60)

# allows us to enter values
entry1 = Entry(root, textvariable=num1)
entry2 = Entry(root, textvariable=num2)
read_result = Entry(root, textvariable=res)

# placing the box for the entries
entry1.place(x=75, y=10)
entry2.place(x=75, y=35)
read_result.place(x=75, y=60)

# defining functions of the buttons
def add():
    one = int(num1.get())
    two = int(num2.get())
    results = one + two
    res.set(results)

def clear():
    entry1.delete(0, END)
    entry2.delete(0,END)
    read_result.delete(0,END)

def ext():
    return root.destroy()

# naming the buttons and giving there functions
addbtn = Button(root, text="ADD", command=add)
clearbtn = Button(root, text="CLEAR", command=clear)
extbtn = Button(root, text="VANISH", command=ext)

# placing the buttons
addbtn.place(x=10, y=100)
clearbtn.place(x=75, y=100)
extbtn.place(x=153, y=100)

# continuosly runs the program window
root.mainloop()
