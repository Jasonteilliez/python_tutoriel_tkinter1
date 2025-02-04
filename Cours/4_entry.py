import tkinter as tk

root = tk.Tk()
root.title("Tutorial Step 4 : Entry")
root.geometry("800x600")

e = tk.Entry(root)
e.pack()
e.insert(0, "Enter Your Name : ")

e2 = tk.Entry(root, width=50, bg='blue', fg='white', borderwidth=5)
e2.pack()

e.get()

def my_click():
    hello = "Hello " + e.get()
    mylabel = tk.Label(root, text=hello)
    mylabel.pack()

my_button = tk.Button(root, text="Enter Your name", padx = 10, pady= 10, command=my_click)
my_button.pack()



root.mainloop()