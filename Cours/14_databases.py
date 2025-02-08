import tkinter as tk
from PIL import ImageTk, Image
import sqlite3

root = tk.Tk()
root.title("Tutorial Step 14 : Databases")
root.iconbitmap('Cours/assets/holo_icon.ico') 
root.geometry("400x400")
    
# Create a database or connect to one
conn = sqlite3.connect('Cours/database/address_book.db')
# Create cursor
c = conn.cursor() 
# Create table
c.execute("""
        CREATE TABLE IF NOT EXISTS addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          zipcode integer
        )
""")
# Commit change 
conn.commit()
# Close Connection
conn.close()


f_name_label = tk.Label(root, text="First Name")
l_name_label = tk.Label(root, text="Last Name")
address_label = tk.Label(root, text="Adresse Name")
city_label = tk.Label(root, text="City Name")
zipcode_label = tk.Label(root, text="Zipcode Name")

f_name = tk.Entry(root, width=30)
l_name = tk.Entry(root, width=30)
address = tk.Entry(root, width=30)
city = tk.Entry(root, width=30)
zipcode = tk.Entry(root, width=30)


f_name_label.grid(row=0, column=0, padx=20)
l_name_label.grid(row=1, column=0, padx=20)
address_label.grid(row=2, column=0, padx=20)
city_label.grid(row=3, column=0, padx=20)
zipcode_label.grid(row=4, column=0, padx=20)

f_name.grid(row=0, column=1, padx=20)
l_name.grid(row=1, column=1, padx=20)
address.grid(row=2, column=1, padx=20)
city.grid(row=3, column=1, padx=20)
zipcode.grid(row=4, column=1, padx=20)

tk.mainloop()