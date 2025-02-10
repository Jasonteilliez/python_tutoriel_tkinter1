import tkinter as tk

class SecondWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Second Window")
        self.geometry("200x150")
        
        label = tk.Label(self, text="This is a second window")
        label.pack(pady=20)

class SideMenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightgray')
        self.init_ui()
    
    def init_ui(self):
        label = tk.Label(self, text="Side Menu", bg='lightgray')
        label.pack(pady=10)
        
        button = tk.Button(self, text="Open Window", command=self.open_window)
        button.pack(pady=5)
    
    def open_window(self):
        SecondWindow(self)

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightblue')
        self.init_ui()
    
    def init_ui(self):
        label = tk.Label(self, text="Hello, Tkinter with Classes!", bg='lightblue')
        label.pack(pady=10)
        
        button = tk.Button(self, text="Click Me", command=self.on_button_click)
        button.pack(pady=5)
    
    def on_button_click(self):
        print("Button clicked!")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter App with Classes")
        self.geometry("400x200")
        
        self.side_menu = SideMenuFrame(self)
        self.side_menu.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        self.frame = MainFrame(self)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()

