#   _________.__    .__.__  __       _________            .___             _______          .__
#  /   _____/|  |__ |__|__|/  |_     \_   ___ \  ____   __| _/____         \      \    ____ |  |
#  \_____  \ |  |  \|  |  \   __\    /    \  \/ /  _ \ / __ |/ __ \        /   |   \  / ___\|  |
#  /        \|   Y  \  |  ||  |      \     \___(  <_> ) /_/ \  ___/       /    |    \/ /_/  >  |__
# /_______  /|___|  /__|__||__|       \______  /\____/\____ |\___  >      \____|__  /\___  /|____/
#         \/      \/                         \/            \/    \/               \//_____/

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.configure(bg="#333333")

root.geometry("600x400")
root.title("Distance Converter")

frame = tk.Frame()
title_label = tk.Label(
    frame, text="Distance Converter", font=("Comic Sans MS", 30), fg="#ffffff"
)
title_label.grid(row=0, column=0, columnspan=2, pady=10)


amount = ttk.Entry(frame, font=("Comic Sans MS", 16), width=25)
amount.grid(row=1, column=0, pady=10)
frame.pack()
variable = tk.StringVar(frame)
variable.set("meter")
res_label = tk.Label(frame, text="", font=("Comic Sans MS", 25), fg="#ffffff")

CONVERTERS = {
    "rod": 0.0606061,
    "kilometer": 0.0003048,
    "meter": 0.3048,
    "centimeter": 30.48,
    "milimeter": 304.8,
    "micrometer": 304800,
    "nanometer": 3.048e8,
    "mile": 0.000189394,
    "yard": 0.33333367016623338674,
    "inch": 12.000012125984401479,
}


def convert_callback():
    value = amount.get()
    convert_to = variable.get()
    try:
        value = int(value)
    except ValueError:
        res_label["text"] = "nahbro please enter an int"
        return

    result = value * CONVERTERS[convert_to]
    res_label[
        "text"
    ] = f"{value} {'foot' if value == 1 else 'feet'} = {result} {convert_to}{'s' if result == 1 else ''}"


def clear_callback():
    variable.set("meter")
    amount.delete(0, tk.END)
    res_label["text"] = ""


lightmode = False


def change_mode():
    global lightmode
    lightmode = not lightmode
    if lightmode:
        root.configure(bg="#ffffff")
        frame.configure(bg="#ffffff")
    else:
        root.configure(bg="#333333")
        frame.configure(bg="#333333")


unit = tk.OptionMenu(frame, variable, *CONVERTERS.keys())
unit.grid(row=2, column=0, columnspan=2, pady=20)

frame2 = tk.Frame()
clear_button = tk.Button(
    frame2, text="Clear", bg="#ffffff", fg="#ff0000", command=clear_callback
)
clear_button.grid(row=3, column=1, columnspan=2, pady=20,padx=50)

convert_button = tk.Button(
    frame2, text="Convert", bg="#ffffff", fg="#ff0000", command=convert_callback
)
convert_button.grid(row=3, column=2, columnspan=2, pady=20,padx=50)

convert_button = tk.Button(
    frame2, text="Light Mode", bg="#ffffff", fg="#ff0000", command=change_mode
)
convert_button.grid(row=3, column=3, columnspan=2, pady=20, padx=50)
frame2.pack()

res_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
