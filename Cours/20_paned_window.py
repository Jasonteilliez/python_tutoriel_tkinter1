import tkinter as tk
import os

basedir = os.path.dirname(__file__)

root = tk.Tk()
root.title("Tutoriel step 20 : Paned window")
root.iconbitmap(os.path.join(basedir, "assets/holo_icon.ico"))
root.geometry('400x400')

# Create a horizontal PanedWindow
paned_window = tk.PanedWindow(root, orient='horizontal')
paned_window.pack(fill='both', expand=True)

# Left frame
left_frame = tk.Frame(paned_window, bg="lightblue", width=150)
paned_window.add(left_frame)

# Right frame
right_frame = tk.Frame(paned_window, bg="lightgreen", width=250)
paned_window.add(right_frame)

# Create a vertical PanedWindow inside the right frame
vertical_pane = tk.PanedWindow(right_frame, orient='vertical')
vertical_pane.pack(fill='both', expand=True)

# Top panel
top_panel = tk.Label(vertical_pane, text="Top Panel", bg="pink", height=5)
vertical_pane.add(top_panel)

# Bottom panel
bottom_panel = tk.Label(vertical_pane, text="Bottom Panel", bg="orange", height=5)
vertical_pane.add(bottom_panel)

root.mainloop()
