import tkinter as tk

def on_button_click(index):
    print(f"Button {index} clicked")

root = tk.Tk()
root.title("Button List Example")

buttons = []

for i in range(5):  # Creating 5 buttons
    btn = tk.Button(root, text=f"Button {i}", command=lambda i=i: on_button_click(i))
    btn.pack(pady=5)
    buttons.append(btn)  # Store buttons in a list if needed

root.mainloop()


