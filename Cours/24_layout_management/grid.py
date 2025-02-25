import tkinter as tk
import os

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 24_2 : Layout Management Grid")
root.iconbitmap(os.path.join(basedir, "../assets/holo_icon.ico"))
root.geometry('400x400')

tk.Label(root, text="Row 0, Col 0", bg="red", fg="white").grid(row=0, column=0)
tk.Label(root, text="Row 0, Col 1", bg="green", fg="white").grid(row=0, column=1)
tk.Label(root, text="Row 1, Col 0", bg="blue", fg="white").grid(row=1, column=0)
tk.Label(root, text="Row 1, Col 1", bg="yellow", fg="black").grid(row=1, column=1)

root.mainloop()