import tkinter as tk
from tkinter import ttk

root = tk.Tk("Test Tkinter App")
label = tk.Label(root, text="Goodbye World")
label.config(font="Times 69")
label.pack()
counter = 0


def callback():
    global counter

    counter += 1
    label["text"] = str(counter)


button = tk.Button(root, text="Click this", command=callback)
button.pack()
root.mainloop()
