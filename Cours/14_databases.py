import tkinter as tk
from PIL import ImageTk, Image
import sqlite3

            
def submit():
    data = {
          "f_name": f_name.get(), 
          "l_name": l_name.get(),
          "address": address.get(),
          "city": city.get(),
          "zipcode": zipcode.get()
    }

    try :
        with conn:
            conn.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :zipcode)", data)
    except sqlite3.Error as e:
        print(e)

    f_name.delete(0, "end"), 
    l_name.delete(0, "end"),
    address.delete(0, "end"),
    city.delete(0, "end"),
    zipcode.delete(0, "end")

def get_all():
    try :
        with conn:
            c = conn.cursor() 
            c.execute("SELECT oid, * FROM addresses")
            response = c.fetchall()
    except sqlite3.Error as e:
        print(e)

    print_data = ""
    for data in response:
        print_data += str(data) + "\n"
    get_all_label.config(text=print_data)

def delete_from_id():
    try :
        with conn:
            conn.execute("DELETE FROM addresses WHERE oid = ?", (delete_entry.get(),))
    except sqlite3.Error as e:
        print(e)

    delete_entry.delete(0, "end")


root = tk.Tk()
root.title("Tutorial Step 14 : Databases")
root.iconbitmap('Cours/assets/holo_icon.ico') 
# root.geometry("400x400")
    
# Create a database or connect to one
conn = sqlite3.connect('Cours/database/address_book.db')

##########################################################################
# try :
#     with conn:
#         conn.execute("""
#         CREATE TABLE IF NOT EXISTS addresses (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           zipcode integer
#         )
# """)
# except sqlite3.Error as e:
#     print(e)

# data = (
#     {"f_name": "John", "l_name": "Dow","address": "24 rue alponse daudet","city": "Auchy","zipcode": 62138},
#     {"f_name": "Jeanne", "l_name": "Aura","address": "32 rue basilick","city": "Bethune","zipcode": 62600},
#     {"f_name": "Leona", "l_name": "Ff","address": "54 ici ou la","city": "Paris","zipcode": 10111},
# )
# try :
#     with conn:
#         conn.executemany("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :zipcode)", data)
# except sqlite3.Error as e:
#     print(e)
##########################################################################

# Create elements
f_name_label = tk.Label(root, text="First Name :")
l_name_label = tk.Label(root, text="Last Name :")
address_label = tk.Label(root, text="Adresse :")
city_label = tk.Label(root, text="City :")
zipcode_label = tk.Label(root, text="Zipcode :")

f_name = tk.Entry(root, width=30)
l_name = tk.Entry(root, width=30)
address = tk.Entry(root, width=30)
city = tk.Entry(root, width=30)
zipcode = tk.Entry(root, width=30)

b_submit = tk.Button(root, text="Submit", command=submit)

b_get_all = tk.Button(root, text="Fetch All", command=get_all)
get_all_label = tk.Label(root)

delete_label = tk.Label(root, text="ID Delete")
delete_entry = tk.Entry(root, width=30)
delete_button = tk.Button(root, text="Delete", command=delete_from_id)

# Add elements to the window
f_name_label.grid(row=0, column=0, padx=(20,5), sticky="e")
l_name_label.grid(row=1, column=0, padx=(20,5), sticky="e")
address_label.grid(row=2, column=0, padx=(20,5), sticky="e")
city_label.grid(row=3, column=0, padx=(20,5), sticky="e")
zipcode_label.grid(row=4, column=0, padx=(20,5), sticky="e")

f_name.grid(row=0, column=1, padx=(5,20))
l_name.grid(row=1, column=1, padx=(5,20))
address.grid(row=2, column=1, padx=(5,20))
city.grid(row=3, column=1, padx=(5,20))
zipcode.grid(row=4, column=1, padx=(5,20))

b_submit.grid(row=5,column=0, columnspan=2,pady=(10,5), padx=20, ipadx=110)

b_get_all.grid(row=6,column=0, columnspan=2,pady=(5,10), padx=20, ipadx=110)
get_all_label.grid(row=7,column=0, columnspan=2)

delete_label.grid(row=8, column=0, padx=(20,5), sticky="e")
delete_entry.grid(row=8, column=1, padx=(5,20))
delete_button.grid(row=9,column=0, columnspan=2,pady=(10,5), padx=20, ipadx=110)

tk.mainloop()
conn.close()