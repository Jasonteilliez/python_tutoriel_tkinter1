import tkinter as tk
import os

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 24_1 : Layout Management Pack")
root.iconbitmap(os.path.join(basedir, "../assets/holo_icon.ico"))
root.geometry('400x400')

tk.Label(root, text="Top", bg="red", fg="white").pack(fill='x')
tk.Label(root, text="Middle", bg="green", fg="white").pack(expand=True, fill='both')
tk.Label(root, text="Bottom", bg="blue", fg="white").pack(fill='x')

root.mainloop()