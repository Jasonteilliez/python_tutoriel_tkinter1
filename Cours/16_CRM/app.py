import tkinter as tk
from database import Database


class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#cccccc")
        self.init_ui()

    def init_ui(self):
        lbl = tk.Label(self, text="Main Frame")
        lbl.pack()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tutorial Step 16 : Customer Relationship Management")
        self.root.iconbitmap('Cours/assets/holo_icon.ico')
        self.root.geometry("400x400")

        self.db = Database()

        self.frame = MainFrame(root)
        self.frame.pack(expand=True, fill='both')
        


