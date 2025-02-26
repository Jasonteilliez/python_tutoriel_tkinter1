import tkinter as tk
from tkinter import ttk
import os

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 25 : Treeview")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')

tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
tree.pack(fill="both", expand=True)

tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

tree.insert("", "end", values=("Alice", 25))
tree.insert("", "end", values=("Bob", 30))
tree.insert("", "end", values=("Charlie", 22))

root.mainloop()