import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

root = tk.Tk()
root.title("Tutorial Step 8 : Message Box")

def popup():
    # messagebox.showinfo("This is my Popup!", "Information")
    # messagebox.showwarning("This is my Popup!", "Warning")
    # messagebox.showerror("This is my Popup!", "Error")
    # messagebox.askquestion("This is my Popup!", "Want something ?")
    # messagebox.askokcancel("This is my Popup!", "Continue ?")
    # messagebox.askyesno("This is my Popup!", "Yes or no ?")
    response = messagebox.askyesno("This is my Popup!", "Yes or no ?")
    if response == 1:
        tk.Label(root, text="Are you sure ?").pack()
    if response == 0:
        tk.Label(root, text="Why not ?").pack()

tk.Button(root, text="Popup", command=popup).pack()

tk.mainloop()