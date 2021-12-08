#Anthony Fagiolo
#December 7th, 2021
#Basic GUI Calculator
import tkinter as tk
root = tk.Tk()
root.title = "Calculator :)"

#operator formulas
def plus_func():
    entry = numb.get()
    entry += "+"
    numb.set(entry)

def minus_func():
    entry = numb.get()
    entry += "-"
    numb.set(entry)

def multiply_func():
    entry = numb.get()
    entry += "*"
    numb.set(entry)

def divide_func():
    entry = numb.get()
    entry += "/"
    numb.set(entry)

def exponet_func():
    entry = numb.get()
    entry += "**"
    numb.set(entry)

def remainder_func():
    entry = numb.get()
    entry += "%"
    numb.set(entry)

def equals_func():
    e = numb.get()
    answer = eval(e)
    numb.set(answer)

#variables i need
numb = tk.StringVar()

#formulas for numbers
def one():
    entry = numb.get()
    entry += "1"
    numb.set(entry)

def two():
    entry = numb.get()
    entry += "2"
    numb.set(entry)

def three():
    entry = numb.get()
    entry += "3"
    numb.set(entry)

def four():
    entry = numb.get()
    entry += "4"
    numb.set(entry)

def five():
    entry = numb.get()
    entry += "5"
    numb.set(entry)

def six():
    entry = numb.get()
    entry += "6"
    numb.set(entry)

def seven():
    entry = numb.get()
    entry += "7"
    numb.set(entry)

def eight():
    entry = numb.get()
    entry += "8"
    numb.set(entry)

def nine():
    entry = numb.get()
    entry += "9"
    numb.set(entry)

def zero():
    entry = numb.get()
    entry += "0"
    numb.set(entry)

#buttons for numbers
numb_button0 = tk.Button(root,text="0", command=zero)
numb_button0.grid(row=6, column=2)
numb_button1 = tk.Button(root, text="1",command=one)
numb_button1.grid(row=3 ,column=1 )
numb_button2 = tk.Button(root, text="2", command=two)
numb_button2.grid(row=3 ,column=2 )
numb_button3 = tk.Button(root, text="3", command=three)
numb_button3.grid(row=3 ,column=3 )
numb_button4 = tk.Button(root, text="4", command=four)
numb_button4.grid(row=4 ,column=1 )
numb_button5 = tk.Button(root, text="5", command=five)
numb_button5.grid(row=4 ,column=2 )
numb_button6 = tk.Button(root, text="6", command=six)
numb_button6.grid(row=4 ,column=3 )
numb_button7 = tk.Button(root, text="7", command=seven)
numb_button7.grid(row=5 ,column=1 )
numb_button8 = tk.Button(root, text="8", command=eight)
numb_button8.grid(row=5,column=2 )
numb_button9 = tk.Button(root, text="9", command=nine)
numb_button9.grid(row=5 ,column=3 )

#buttons for arithmetic
plus_button = tk.Button (root, text="+", command=plus_func)
plus_button.grid(row=3 , column=4 )
minus_button = tk.Button (root, text="-", command=minus_func)
minus_button.grid(row=3, column=5)
multiply_button = tk.Button(root, text="*", command=multiply_func)
multiply_button.grid(row=4,column=4)
divide_button = tk.Button(root, text="/", command=divide_func)
divide_button.grid(row=4,column=5)
exponet_button = tk.Button(root, text="^", command=exponet_func)
exponet_button.grid(row=5,column=4)
remainder_button = tk.Button(root, text="%", command=remainder_func)
remainder_button.grid(row=5,column=5)
equals_button = tk.Button(root,text="=", command=equals_func)
equals_button.grid(row=6,column=4,columnspan=2)

#entry field
numb_entry = tk.Entry(root, textvariable=numb)
numb_entry.grid(row=1,column=1, columnspan=5)






root.mainloop()