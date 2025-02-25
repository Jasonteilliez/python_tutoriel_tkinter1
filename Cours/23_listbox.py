import tkinter as tk
from tkinter import messagebox
import os

def add_item():
    item = entry.get()
    if item:
        listbox.insert('end', item)
        entry.delete(0, 'end')
    else:
        messagebox.showwarning("Warning", "Please enter an item!")

def remove_item():
    try:
        # selected_index = listbox.curselection()[0]
        # listbox.delete(selected_index)
        listbox.delete('anchor')
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to remove!")

def get_selected_item():
    try:
        # selected_index = listbox.curselection()[0]
        # selected_text = listbox.get(selected_index)
        selected_text = listbox.get('anchor')
        messagebox.showinfo("Selected Item", f"You selected: {selected_text}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item!")

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 23 : Listbox")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, height=10, width=30, selectmode='single')
listbox.pack(side='left', fill='y')

scrollbar = tk.Scrollbar(frame, orient='vertical')
scrollbar.pack(side='right', fill='y')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack(pady=5)

select_button = tk.Button(root, text="Get Selected Item", command=get_selected_item)
select_button.pack(pady=5)

item_list = ['Apple','Tomato','Banana', 'Cabbage', 'Cucumber', 'Watermelon', 'Parsley', 'Kiwi', 'Grape', 'Ginger', 'Eggplant', 'Celery', 'Carrot']

for item in item_list:
    listbox.insert('end', item)

root.mainloop()