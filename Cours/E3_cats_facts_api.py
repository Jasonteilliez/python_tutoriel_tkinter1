import tkinter as tk
from PIL import ImageTk, Image
import requests
import json


class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#cccccc")

        self.api_request = ""
        self.api = ""
        self.label_fact_list = []

        self.load_api()
        self.init_ui()

    def init_ui(self):

        # create widget
        label_hello = tk.Label(self, text="Did you know ?", font=("Helvetica",15))

        if self.api :
            for data in self.api :
                label_facts = tk.Label(self, text=data['text'], font=("Helvetica",12))
                self.label_fact_list.append(label_facts)

        # display widget
        label_hello.grid(row=0, column=0, padx=10, pady=10)

        for key, label in enumerate(self.label_fact_list) : 
            label.grid(row=key+1, column=0, padx=10, pady=10, sticky="w")

    def load_api(self):
        try :
            self.api_request = requests.get("https://cat-fact.herokuapp.com/facts")
            self.api = json.loads(self.api_request.content)
        except Exception as a :
            self.api_request = ""
            self.api = ""


class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title("Cats Facts Api")
        self.iconbitmap('Cours/assets/holo_icon.ico')

        self.frame = MainFrame(self)
        self.frame.pack(expand=True, fill=tk.BOTH)
        

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

app = App()
app.mainloop()