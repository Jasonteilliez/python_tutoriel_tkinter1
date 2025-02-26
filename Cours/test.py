import tkinter as tk

def open_file():
    print("Open File Clicked")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Menu Example")

# Create Menu Bar
menu_bar = tk.Menu(root)

# Create File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Add File Menu to Menu Bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure window to use menu
root.config(menu=menu_bar)

root.mainloop()