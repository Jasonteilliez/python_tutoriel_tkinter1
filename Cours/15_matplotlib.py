import tkinter as tk
from PIL import ImageTk, Image


class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#cccccc")
        self.init_ui()

    def init_ui(self):
        pass

import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#cccccc")
        self.init_ui()

    def init_ui(self):
        btn = tk.Button(self, text="Graph It!", command=(self.graph))
        btn.pack()

    def graph(self):
        house_price = np.random.normal(200000,25000,5000)
        plt.hist(house_price,50) 
        plt.show()                     


class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title("Title")
        self.iconbitmap('Cours/assets/holo_icon.ico')
        self.geometry('400x400')

        self.frame = MainFrame(self)
        self.frame.pack(expand=True, fill='both')
        

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

app = App()
app.mainloop()
class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title("Tutoriel step 15 : Mathplotlib")
        self.iconbitmap('Cours/assets/holo_icon.ico')
        self.geometry('400x400')

        self.frame = MainFrame(self)
        self.frame.pack(expand=True, fill='both')
        

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

app = App()
app.mainloop()