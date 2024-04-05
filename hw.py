from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.pack()

a = Label(root, text="1", width=2, font=("Helvetica", 300))
a.pack()

root.mainloop()
