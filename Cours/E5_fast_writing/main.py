import tkinter as tk
import time
from os import path

class FelicitationWindow(tk.Toplevel):
    def __init__(self, parent, reset, elapsed):
        super().__init__(parent)
        self.basedir = path.dirname(__file__)

        self.title("Fast Writing Felicitation")
        self.iconbitmap(path.join(self.basedir, "images/fw_icon.ico"))
        self.geometry("400x200")

        self.reset=reset
        self.elapsed = elapsed
        self.minutes = int(self.elapsed // 60)
        self.seconds = int(self.elapsed % 60)
        self.milliseconds = int((self.elapsed * 1000) % 1000)

        self.init_ui()

    def init_ui(self):

        label_felicitation = tk.Label(self, text="Félicitation", font=("Helvetica", "20", "bold"), padx=20, pady=20)
        label_felicitation.pack()
        label_time = tk.Label(self, text="Vous avez mis {:02}m {:02}s {:03}ms".format(self.minutes,self.seconds,self.milliseconds))
        label_time.pack()
        button_reset = tk.Button(self, text="Recommencer", command=self.restart)
        button_reset.pack(padx=20, pady=20)

    def restart(self):
        self.reset()
        self.destroy()


class App:
    def __init__(self, root):
        self.root = root
        self.basedir = path.dirname(__file__)

        self.root.title("Fast Writing")
        self.root.iconbitmap(path.join(self.basedir, "images/fw_icon.ico"))
        self.root.bind("<KeyPress>", self.tap_key)

        self.text = ""
        self.writen_text = ""
        self.n_char = 0
        self.text_active = False

        # timer
        self.running = False
        self.start_time = 0

        self.init_ui()

    def init_ui(self):
        frame_text_selection = tk.Frame(root, padx=10, pady=10)
        label_enter = tk.Label(frame_text_selection, text="Entrez votre text :")
        self.entry_text = tk.Entry(frame_text_selection, width=50)
        self.button_comfirmer = tk.Button(frame_text_selection, text="valider", command=self.valider_text)
        self.label_timer = tk.Label(frame_text_selection, text="00:00:000")

        frame_text_exercice = tk.Frame(root, padx=10, pady=10)
        self.text_widget = tk.Text(frame_text_exercice, wrap="word", width=50, height=10)
        self.text_widget.config(state="disabled")
        self.text_widget.tag_config("correct_text", foreground="#09571D",background="#BAD1C0")
        self.text_widget.tag_config("wrong_text", foreground="#7D090C", background="#CCA5A6")  

        button_reset = tk.Button(frame_text_exercice, text="Reset", command=self.reset)

        frame_text_selection.pack(fill="x")
        label_enter.grid(row=0, column=0)
        self.entry_text.grid(row=0, column=1)
        self.button_comfirmer.grid(row=1, column=0, sticky='w', pady=(10,0))
        self.label_timer.grid(row=1, column=1, sticky='e')

        frame_text_exercice.pack(fill="x")
        self.text_widget.grid(row=0, column=0)
        button_reset.grid(row=1,column=0, pady=(10,0), sticky='w')

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
        self.button_comfirmer.config(state="disabled")
        
        self.root.focus_set()
        
    def tap_key(self, event):
        if not self.text_active:
            return
        if event.keycode == 8 and self.n_char!=0:
            self.n_char-=1
            self.text_widget.tag_remove("correct_text", "1.{}".format(str(self.n_char)), "end")
            self.text_widget.tag_remove("wrong_text", "1.{}".format(str(self.n_char)), "end")
            self.writen_text = self.writen_text[:-1]
        if event.char and self.n_char < len(self.text) and event.char not in '\x08\n\r\t':
            self.start_timer()
            self.compare_character(event.char, self.text[self.n_char])
            self.n_char+=1
            self.writen_text += event.char
        if self.writen_text == self.text:
            self.victoire()

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
        self.button_comfirmer.config(state="normal")

        self.text_widget.config(state="normal")
        self.text_widget.delete("1.0", "end")
        self.text_widget.config(state="disabled")

        self.reset_timer()
        
    def victoire(self):
        elapsed = time.time() - self.start_time
        FelicitationWindow(root, self.reset, elapsed)
        self.text_active = False
        self.stop_timer()

    def update_timer(self):
        if not self.running:
            return
        elapsed = time.time() - self.start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed * 1000) % 1000)

        self.label_timer.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:03}")
        self.root.after(10, self.update_timer)

    def start_timer(self):
        if self.running:
            return
        self.start_time = time.time()
        self.running = True
        self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.start_time = 0
        self.label_timer.config(text="00:00:000")
        

root = tk.Tk()
app = App(root)
root.mainloop() 