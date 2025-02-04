import tkinter as tk
from PIL import ImageTk, Image

# def update_horizontal(value):
#     root.geometry(f"{300+int(value)}x{300+vertical.get()}")


# def update_vertical(value):
#     root.geometry(f"{300+horizontal.get()}x{300+int(value)}")
    
def update_window(value):
    root.geometry(f"{300+horizontal.get()}x{300+vertical.get()}")

root = tk.Tk()
root.title("Tutorial Step 11 : Sliders")
root.iconbitmap('Cours/assets/holo_icon.ico')
root.geometry("300x300")

# vertical = tk.Scale(root, from_=0, to=200, length=200, command=update_vertical)
vertical = tk.Scale(root, from_=0, to=200, length=200, command=update_window)
vertical.pack()

# horizontal = tk.Scale(root, from_=0, to=200, orient="horizontal", length=200, command=update_horizontal)
horizontal = tk.Scale(root, from_=0, to=200, orient="horizontal", length=200, command=update_window)
horizontal.pack()


tk.mainloop()