import tkinter as tk

root = tk.Tk()
root.title("Tutorial Step 2 : Grid")
root.geometry("800x600")

label1 = tk.Label(root, text="Hello World!")
label2 = tk.Label(root, text="My name is ...")
label3 = tk.Label(root, text="fdjkdjlkjflkjdk").grid(row=2, column=2)


label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

root.mainloop()