import tkinter as tk
from PIL import ImageTk, Image

def change_image(direction):
    global my_label
    global current_image
    global total_image
    global status_barre

    if direction:
        current_image += 1
    if not direction:
        current_image -= 1

    if current_image>= total_image:
        current_image=0
    if current_image<0:
        current_image= total_image-1

    my_label.destroy()
    my_label= tk.Label(root, image=image_list[current_image])
    my_label.grid(row=0, column=0, columnspan=3)

    status_barre.destroy()
    status_barre = tk.Label(root, text="Image " + str(current_image+1)+ " / " + str(total_image), bd=1, relief="sunken", anchor="e")
    status_barre.grid(row=2, column=0, columnspan=3, sticky="we")


root = tk.Tk()
root.title("image viewing app")
root.iconbitmap('Cours/assets/holo_icon.ico') 

my_image1 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco1.jpg").resize((500,500)))
my_image2 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco2.jpg").resize((500,500)))
my_image3 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco3.jpg").resize((500,500)))
my_image4 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco4.jpg").resize((500,500)))
my_image5 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco5.jpg").resize((500,500)))
my_image6 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco6.jpg").resize((500,500)))
my_image7 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco7.jpg").resize((500,500)))
my_image8 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco8.jpg").resize((500,500)))
my_image9 = ImageTk.PhotoImage(Image.open("Cours/assets/fuzichoco9.jpg").resize((500,500)))

image_list = [my_image1,my_image2,my_image3,my_image4,my_image5,my_image6,my_image7,my_image8,my_image9]
current_image = 0 
total_image = len(image_list)

my_label= tk.Label(root, image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = tk.Button(root,text="<<", command=lambda: change_image(0))
button_exit = tk.Button(root,text="EXIT", command=root.quit)
button_forward = tk.Button(root,text=">>", command=lambda: change_image(1))

button_back.grid(row=1, column=0, pady=10)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2, pady=10)

status_barre = tk.Label(root, text="Image " + str(current_image+1)+ " / " + str(total_image), bd=1, relief="sunken", anchor="e")
status_barre.grid(row=2, column=0, columnspan=3, sticky="we")

root.mainloop()