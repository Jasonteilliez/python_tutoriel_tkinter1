import tkinter as tk
import os

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 24_3 : Layout Management Place")
root.iconbitmap(os.path.join(basedir, "../assets/holo_icon.ico"))
root.geometry('400x400')

tk.Label(root, text="Top Left", bg="red", fg="white").place(x=10, y=10)
tk.Label(root, text="Center", bg="green", fg="white").place(x=120, y=80)
tk.Label(root, text="Bottom Right", bg="blue", fg="white").place(x=200, y=150)

root.mainloop()