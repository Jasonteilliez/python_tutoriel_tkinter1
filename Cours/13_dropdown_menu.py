import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Tutoriel step 13 : DropDown Menu")
root.iconbitmap('Cours/assets/holo_icon.ico')
root.geometry("400x400")

def selected(event):
    label.config(text=f"Selected: {clicked.get()}")

def show():
    label2.config(text=f"Selected: {clicked.get()}")

option_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = tk.StringVar()
clicked.set(option_list[0])

# OptionMenu widget only allows the user to choose an option that is in the menu.
# Combobox widget essentially combines an Entry widget with the OptionMenu widget.
# # state="readonly" to deactived the Entry widget.
dropdown1 = tk.OptionMenu(root, clicked, *option_list, command=selected)
dropdown2 = ttk.Combobox(root, textvariable=clicked, values=option_list, state="readonly")
dropdown2.bind("<<ComboboxSelected>>", selected)

label = tk.Label(root, text=f"Selected: {clicked.get()}")
label2 = tk.Label(root, text=f"Selected: {clicked.get()}")

button = tk.Button(root, text="Show Selection", command=show)

dropdown1.pack()
dropdown2.pack()
label.pack()
button.pack()
label2.pack()

tk.mainloop()
