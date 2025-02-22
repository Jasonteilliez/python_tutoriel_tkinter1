import tkinter as tk
import os

def open_file():
    print("Open File clicked!")

def save_file():
    print("Save File clicked!")

def exit_app():
    root.quit()  # Close the application

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 19 : Menu")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')

# Create the top menu bar
menu_bar = tk.Menu(root)

# ---- File Menu ----
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()  # Add a separator line
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# ---- Edit Menu ----
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: print("Undo clicked"))
edit_menu.add_command(label="Redo", command=lambda: print("Redo clicked"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Set the menu bar in the application
root.config(menu=menu_bar)

root.mainloop()