import tkinter as tk
import os

def open_file():
    hide_frame()
    frame_open.pack(expand=True, fill='both')

def save_file():
    hide_frame()
    frame_save.pack(expand=True, fill='both')

def undo():
    hide_frame()
    frame_undo.pack(expand=True, fill='both')

def redo():
    hide_frame()
    frame_redo.pack(expand=True, fill='both')

def hide_frame():
    frame_open.pack_forget()
    frame_save.pack_forget()
    frame_undo.pack_forget()
    frame_redo.pack_forget()


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
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Set the menu bar in the application
root.config(menu=menu_bar)

frame_open = tk.Frame(root)
frame_save = tk.Frame(root)
frame_undo = tk.Frame(root)
frame_redo = tk.Frame(root)

label_open = tk.Label(frame_open, text="Open menu").pack()
label_save = tk.Label(frame_save, text="Save menu").pack()
label_undo = tk.Label(frame_undo, text="Undo menu").pack()
label_redo = tk.Label(frame_redo, text="Redo menu").pack()


root.mainloop()