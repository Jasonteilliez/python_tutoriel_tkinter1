import tkinter as tk

root = tk.Tk()
root.title("Tutorial step 9 : New Window")
root.geometry("500x500")


def open():
    top = tk.Toplevel()
    top.geometry("500x500")
    top.title("2nd window")
    label = tk.Label(top, text="Hello second window").pack()
    bnt2 = tk.Button(top, text="close", command=top.destroy).pack()


label = tk.Label(root, text="Hello main window").pack()
btn = tk.Button(root, text="Open second window", command=open).pack()


tk.mainloop()