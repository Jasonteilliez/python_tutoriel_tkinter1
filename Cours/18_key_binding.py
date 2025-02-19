import tkinter as tk
import os

basedir = os.path.dirname(__file__)

def clicker(event):
    label_test.config(text='You clicked a button'+ str(event.x) + " " + str(event.y))

root = tk.Tk()
root.title("Tutoriel step 18 : Key Binding")
root.iconbitmap(os.path.join(basedir, "assets\holo_icon.ico"))
root.geometry('400x400')

button_test = tk.Button(root, text='Click Me')
button_test.bind("<Button-1>", clicker) # left click
# button_test.bind("<Button-3>", clicker) # right click
# button_test.bind("<Enter>", clicker) # enter widget
# button_test.bind("<Leave>", clicker) # leave widget
# button_test.bind("<FocusIn>", clicker) # focus on widget

label_test = tk.Label(root)

button_test.pack(pady=20)
label_test.pack()

root.mainloop()