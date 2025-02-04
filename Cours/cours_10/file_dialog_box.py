import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog,messagebox

def open():
    try : 
        filename = filedialog.askopenfilename(initialdir='Cours/cours_10/assets', title="Select a File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.ico"),("All Files", '*.*')])
        if filename :
            img = Image.open(filename)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            image_tk = ImageTk.PhotoImage(img)
            my_label.config(image=image_tk)
            my_label.image = image_tk
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

root = tk.Tk()
root.title("Tutorial Step 10 : File Dialog Box")
root.iconbitmap('Cours/cours_10/assets/holo_icon.ico') 
root.geometry("400x400")
    
btn = tk.Button(root, text="Open file", command=open)
btn.pack(pady=10)

my_label = tk.Label(root)
my_label.pack()

tk.mainloop()