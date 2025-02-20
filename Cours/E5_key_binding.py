import tkinter as tk
from os import path

class App:
    def __init__(self, root):
        self.root = root
        self.basedir = path.dirname(__file__)

        self.root.title("Tutorial Step 16 : Customer Relationship Management")
        self.root.iconbitmap(path.join(self.basedir, "assets/holo_icon.ico"))
        self.root.bind("<KeyPress>", self.tap_key)

        self.legal_character = """azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBNéèêëàâîïùç1234567890°'".,;:?!_()}{[]+-/*=@#$€& """

        self.text = ""
        self.writen_text = ""
        self.n_char = 0
        self.text_active = False

        self.init_ui()

    def init_ui(self):
        frame_text_selection = tk.Frame(root, padx=10, pady=10)
        label_enter = tk.Label(frame_text_selection, text="Entrez votre text :")
        self.entry_text = tk.Entry(frame_text_selection, width=50)
        button_comfirmer = tk.Button(frame_text_selection, text="valider", command=self.valider_text)

        frame_text_exercice = tk.Frame(root, padx=10, pady=10)
        self.text_widget = tk.Text(frame_text_exercice, wrap="word", width=50, height=10)
        self.text_widget.config(state="disabled")
        self.text_widget.tag_config("correct_text", foreground="#09571D",background="#BAD1C0")
        self.text_widget.tag_config("wrong_text", foreground="#7D090C", background="#CCA5A6")  

        button_reset = tk.Button(frame_text_exercice, text="Reset", command=self.reset)

        frame_text_selection.pack(fill="x")
        label_enter.grid(row=0, column=0)
        self.entry_text.grid(row=0, column=1)
        button_comfirmer.grid(row=1, column=0, sticky='w', pady=(10,0))

        frame_text_exercice.pack(fill="x")
        self.text_widget.grid(row=0, column=0)
        button_reset.grid(row=1,column=0, sticky='w')

    def valider_text(self):
        self.text = self.entry_text.get()
        self.text = self.text.strip()
        if self.text == "" :
            return
        
        self.entry_text.config(state="readonly")
        self.text_active = True

        self.text_widget.config(state="normal")
        self.text_widget.insert("1.0", self.text)
        self.text_widget.config(state="disabled")
        
        self.root.focus_set()
        
    def tap_key(self, event):
        if not self.text_active:
            return
        if event.keycode == 8 and self.n_char!=0:
            self.n_char-=1
            self.text_widget.tag_remove("correct_text", "1.{}".format(str(self.n_char)), "end")
            self.text_widget.tag_remove("wrong_text", "1.{}".format(str(self.n_char)), "end")
        if event.char and event.char in self.legal_character and self.n_char < len(self.text):
            self.compare_character(event.char, self.text[self.n_char])
            self.n_char+=1

    def compare_character(self, char1, char2):
        if (char1 == char2):
            self.text_widget.tag_add("correct_text", "1.{}".format(str(self.n_char)), "1.{}".format(str(self.n_char+1)))
            return
        self.text_widget.tag_add("wrong_text", "1.{}".format(str(self.n_char)), "1.{}".format(str(self.n_char+1)))

    def reset(self):
        self.text = ""
        self.writen_text = ""
        self.n_char = 0
        self.text_active = False

        self.entry_text.config(state="normal")

        self.text_widget.config(state="normal")
        self.text_widget.delete("1.0", "end")
        self.text_widget.config(state="disabled")

root = tk.Tk()
app = App(root)
root.mainloop() 