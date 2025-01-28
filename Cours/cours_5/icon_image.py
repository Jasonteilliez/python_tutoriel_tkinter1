import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Tutorial Step 5 : Icon and Image')
#root.iconbitmap('C:/Users/Developpement/python_tutoriel_tkinter1/Cours/cours_5/assets/holo_icon.ico') 
root.iconbitmap('Cours/cours_5/assets/holo_icon.ico') 

my_img = ImageTk.PhotoImage(Image.open("Cours/cours_5/assets/holo.png"))
my_label = tk.Label(image=my_img)
my_label.pack()

button_quit = tk.Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()