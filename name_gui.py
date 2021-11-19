import tkinter as tk

root = tk.Tk()
root.title("Name")

def saying_hello():
    message = "Hello, " + name_entry.get()
    word.set(message)

name = tk.StringVar()
word = tk.StringVar()

name_entry = tk.Entry(root, textvariable=name)
name_entry.grid(row=1,column=1)

say_hello = tk.Button(root, text="Say Hello", command=saying_hello)
say_hello.grid(row=3, column=1)

said_hello = tk.Label(root, textvariable=word)
said_hello.grid(row=2,column=1)



root.mainloop()