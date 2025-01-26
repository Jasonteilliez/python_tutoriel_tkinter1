import tkinter as tk

root = tk.Tk()
root.title("Tutorial Step 3 : Button")
root.geometry("800x600")


def myclick():
    mylabel = tk.Label(root, text="i clicked")
    mylabel.pack()


button = tk.Button(root, text="click me", padx = 10, pady= 10, command=myclick)
button2 = tk.Button(root, text="don't click me", state="disabled")
button3 = tk.Button(root, text="color me", fg="red", bg="#000000")

button.pack()
button2.pack()
button3.pack()


root.mainloop()