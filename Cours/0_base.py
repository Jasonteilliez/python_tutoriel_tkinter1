import tkinter as tk
import os

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 0 : ")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')



root.mainloop()