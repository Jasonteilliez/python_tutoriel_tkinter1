import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Tutorial Step 6 : Frame")

frame = tk.LabelFrame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

b = tk.Button(frame, text="don't click here")
b.pack()

root.mainloop()