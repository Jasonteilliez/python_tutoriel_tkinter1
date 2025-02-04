import tkinter as tk
from PIL import ImageTk,Image

def show_selection():
    selected_options = []
    if var1.get():
        selected_options.append("python")
    if var2.get():
        selected_options.append("C++")
    if var3.get():
        selected_options.append("java")
    
    lbl.config(text="I like " + ", ".join(selected_options) if selected_options else "I don't like code.")

def show_on_off():
    print(var4.get())
    lbl.config(text=var4.get())


root = tk.Tk()
root.title("Tutorial Step 12 : Checkbox")
root.geometry("400x400")
root.iconbitmap('Cours/assets/holo_icon.ico')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

c1 = tk.Checkbutton(root, text='Python',variable=var1, command=show_selection)
c2 = tk.Checkbutton(root, text='C++',variable=var2, command=show_selection)
c3 = tk.Checkbutton(root, text='Java',variable=var3, command=show_selection)

c1.pack()
c2.pack()
c3.pack()

lbl = tk.Label(root, text="I don't like code.")
lbl.pack(pady=10)

var4 = tk.StringVar()
var4.set("Off")
c4 = tk.Checkbutton(root, text='Java',variable=var4, onvalue="On", offvalue="Off", command=show_on_off)
c4.pack()
lbl = tk.Label(root, text="Off")
lbl.pack(pady=10)

root.mainloop()