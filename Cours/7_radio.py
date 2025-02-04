import tkinter as tk

def clicked():
    my_label.config(text = "You have selected option " + str(r1.get()))

def choice():
    my_label2.config(text = "You have selected option " + r2.get())

root = tk.Tk()
root.title("Tutorial Step 7 : Radio Button")

r1 = tk.IntVar()
r1.set(1)

tk.Radiobutton(root, text="Option 1", variable=r1, value=1, command=clicked).pack()
tk.Radiobutton(root, text="Option 2", variable=r1, value=2, command=clicked).pack()
tk.Radiobutton(root, text="Option 3", variable=r1, value=3, command=clicked).pack()

my_label = tk.Label(root)
my_label.pack()

MODES = [
    ("avion","avion"),
    ("bateau","bateau"),
    ("voiture","voiture"),
    ("vélo","vélo"),
    ("pied","pied"),
]

r2 = tk.StringVar()
r2.set(" ")

for text, mode in MODES:
    tk.Radiobutton(root, text=text, variable=r2, value=mode, command=choice).pack(anchor="w")


my_label2 = tk.Label(root, text="chose 1 option")
my_label2.pack()

root.mainloop()