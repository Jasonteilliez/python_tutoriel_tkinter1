import tkinter as tk

def update_color():
    # Remove the existing tag
    text_widget.tag_remove("colored", "1.9", "1.21")  # Removing old tag

    # Add new text
    text_widget.insert("1.5", "NEW ")  # Insert new text at a new position
    text_widget.tag_add("colored", "1.5", "1.9")  # Apply color to the new text

root = tk.Tk()
root.geometry("300x200")

text_widget = tk.Text(root, wrap="word", height=2, width=30)
text_widget.insert("1.0", "This is a ")
text_widget.insert("1.9", "colored text!")

# Initial color tag
text_widget.tag_add("colored", "1.9", "1.21")  
text_widget.tag_config("colored", foreground="red")

# Button to update colored text
button = tk.Button(root, text="Change Color", command=update_color)
button.pack(pady=5)

text_widget.pack(pady=10)

root.mainloop()
