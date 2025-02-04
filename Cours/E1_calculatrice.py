import tkinter as tk



def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current + number)

def clear_click():
    e.delete(0, tk.END)

def add_click():
    number_1 = e.get()
    global first_number
    global math
    math = "addition"
    first_number = int(number_1)
    e.delete(0, tk.END)

def subtract_click():
    number_1 = e.get()
    global first_number
    global math
    math = "subtraction"
    first_number = int(number_1)
    e.delete(0, tk.END)

def multiply_click():
    number_1 = e.get()
    global first_number
    global math
    math = "multiplication"
    first_number = int(number_1)
    e.delete(0, tk.END)

def divide_click():
    number_1 = e.get()
    global first_number
    global math
    math = "division"
    first_number = int(number_1)
    e.delete(0, tk.END) 

def equal_click():
    second_number = e.get()
    e.delete(0, tk.END)
    if math == "addition":
        e.insert(0, first_number + int(second_number)) 
    if math == "subtraction":
        e.insert(0, first_number - int(second_number)) 
    if math == "multiplication":
        e.insert(0, first_number * int(second_number))
    if math == "division":
        e.insert(0, first_number / int(second_number))
         

root = tk.Tk()
root.title("Calulatrice")

e= tk.Entry(root, width=46, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click('1'))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click('2'))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click('3'))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click('4'))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click('5'))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click('6'))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click('7'))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click('8'))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click('9'))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click('0'))

button_add = tk.Button(root, text="+", padx=39, pady=20, command=add_click)
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=subtract_click)
button_multiply = tk.Button(root, text="*", padx=41, pady=20, command=multiply_click)
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=divide_click)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=equal_click)

button_clear = tk.Button(root, text="C", padx=39, pady=20, command=clear_click)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_clear.grid(row=4, column=2)




root.mainloop()