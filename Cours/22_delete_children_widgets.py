import tkinter as tk
from tkinter import colorchooser
import os

def add_label():
    label = tk.Label(frame_label, text="New label")
    label.pack()

def delete_label():
    for widget in frame_label.winfo_children():
        widget.destroy()

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 22 : Delete Children Widgets")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')

frame_button = tk.Frame(root)
frame_label = tk.Frame(root)

button_add_label = tk.Button(frame_button, text="Add label", command=add_label)
button_delete_label = tk.Button(frame_button, text="Delete label", command=delete_label)

frame_button.pack()
frame_label.pack()

button_add_label.grid(row=0, column=0)
button_delete_label.grid(row=0, column=1)


root.mainloop()