import tkinter as tk
from tkinter import colorchooser
import os

def pick_color():
    color = colorchooser.askcolor(title="choose a color")
    if color[1]:
        label_color.config(text=f"Selected Color: {color[1]}", bg=color[1])
    else :
        label_color.config(text="No color selected", bg="white")

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 21 : Color Picker")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')

button_pick = tk.Button(root, text="Pick a Color", command=pick_color)
label_color = tk.Label(root, text="No color selected", bg="white")

button_pick.pack()
label_color.pack()

root.mainloop()