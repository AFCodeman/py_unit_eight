import tkinter as tk

root = tk.Tk()
root.title("Hello")

hi = tk.Label(root, text="Hello, World")
hi.grid(row=1,column=1)


root.mainloop()