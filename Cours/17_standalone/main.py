import tkinter as tk
import os
from PIL import ImageTk, Image
import random

basedir = os.path.dirname(__file__)

def select_random_winner():
    label_winner.config(text=random.choice(list(names)))

root = tk.Tk()
root.title("Random Winner Generator")
root.iconbitmap(os.path.join(basedir, "assets\images\icon.ico"))
root.geometry('400x400')

names = set([
    "Liam Johnson", "Emma Thompson", "Noah Brown", "Olivia Wilson", "Ava Martinez",
    "Sophia Anderson", "Isabella Taylor", "Mia Thomas", "Amelia White", "Harper Harris",
    "Evelyn Martin", "Abigail Clark", "Ella Lewis", "Elizabeth Lee", "Sofia Walker",
    "Avery Hall", "Scarlett Young", "Grace King", "Chloe Wright", "Victoria Scott",
    "Luna Green", "Hannah Adams", "Lily Nelson", "Addison Hill", "Eleanor Carter",
    "Natalie Rivera", "Penelope Cooper", "Zoe Baker", "Stella Gonzalez", "Hazel Roberts",
    "Violet Perez", "Aurora Turner", "Savannah Phillips", "Brooklyn Campbell", "Bella Parker",
    "Claire Evans", "Skylar Edwards", "Lucy Collins", "Paisley Stewart", "Everly Sanchez",
    "Anna Morris", "Caroline Rogers", "Nova Reed", "Genesis Cook", "Kennedy Morgan",
    "Aubrey Bell", "Madelyn Murphy", "Naomi Bailey", "Serenity Rivera", "Nevaeh Howard",
    "Willow Ward", "Camila Cox"
])

label_top = tk.Label(root, text="Win-O-Rama!", font=('Helvetica',24))
label_top.pack(pady=20)

button_win = tk.Button(root,text=' PICK OUR WINNER !', font=('Helvetiva',24), command = select_random_winner)
button_win.pack(pady=20)

label_winner = tk.Label(root, font=('Helvetica',24))
label_winner.pack(pady=20)

root.mainloop()