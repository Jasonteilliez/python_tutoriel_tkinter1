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

def get_from_id(id):
    try :
        with conn:
            c = conn.cursor() 
            c.execute("SELECT * FROM addresses WHERE oid = ?", (id,))
            return c.fetchone()
    except sqlite3.Error as e:
        print(e)

def delete_from_id():
    try :
        with conn:
            conn.execute("DELETE FROM addresses WHERE oid = ?", (select_entry.get(),))
    except sqlite3.Error as e:
        print(e)

    select_entry.delete(0, "end")

def update_from_id(data):
    try :
        with conn:
            conn.execute("""UPDATE addresses SET 
                first_name = :f_name, 
                last_name = :l_name, 
                address = :address, 
                city = :city, 
                zipcode = :zipcode 
                WHERE oid = :oid""",
                data
            )
    except sqlite3.Error as e:
        print(e)

def open_update_window():
    id = select_entry.get()

    response = get_from_id(id)

    update_window = tk.Toplevel()
    update_window.iconbitmap('Cours/assets/holo_icon.ico')
    update_window.title("Update")

    update_f_name_label = tk.Label(update_window, text="First Name :")
    update_l_name_label = tk.Label(update_window, text="Last Name :")
    update_address_label = tk.Label(update_window, text="Adresse :")
    update_city_label = tk.Label(update_window, text="City :")
    update_zipcode_label = tk.Label(update_window, text="Zipcode :")

    update_f_name = tk.Entry(update_window, width=30)
    update_l_name = tk.Entry(update_window, width=30)
    update_address = tk.Entry(update_window, width=30)
    update_city = tk.Entry(update_window, width=30)
    update_zipcode = tk.Entry(update_window, width=30)

    update_f_name.insert("end",response[0])
    update_l_name.insert("end",response[1])
    update_address.insert("end",response[2])
    update_city.insert("end",response[3])
    update_zipcode.insert("end",response[4])

    update_button = tk.Button(update_window, text="Update", command=lambda:update_from_id(
        {
          "oid": id,
          "f_name": update_f_name.get(), 
          "l_name": update_l_name.get(),
          "address": update_address.get(),
          "city": update_city.get(),
          "zipcode": update_zipcode.get()
        }
    ))


    update_f_name_label.grid(row=0, column=0, padx=(20,5), sticky="e")
    update_l_name_label.grid(row=1, column=0, padx=(20,5), sticky="e")
    update_address_label.grid(row=2, column=0, padx=(20,5), sticky="e")
    update_city_label.grid(row=3, column=0, padx=(20,5), sticky="e")
    update_zipcode_label.grid(row=4, column=0, padx=(20,5), sticky="e")

    update_f_name.grid(row=0, column=1, padx=(5,20))
    update_l_name.grid(row=1, column=1, padx=(5,20))
    update_address.grid(row=2, column=1, padx=(5,20))
    update_city.grid(row=3, column=1, padx=(5,20))
    update_zipcode.grid(row=4, column=1, padx=(5,20))

    update_button.grid(row=5,column=0, columnspan=2,pady=(10,5), padx=20, ipadx=107)

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

select_label = tk.Label(root, text="Select ID")
select_entry = tk.Entry(root, width=30)

delete_button = tk.Button(root, text="Delete", command=delete_from_id)

open_update_button = tk.Button(root, text="Update", command=open_update_window)

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

b_get_all.grid(row=6,column=0, columnspan=2,pady=(5,10), padx=20, ipadx=106)
get_all_label.grid(row=7,column=0, columnspan=2)

select_label.grid(row=8, column=0, padx=(20,5), sticky="e")
select_entry.grid(row=8, column=1, padx=(5,20))

delete_button.grid(row=9,column=0, columnspan=2,pady=(10,5), padx=20, ipadx=110)

open_update_button.grid(row=10,column=0, columnspan=2,pady=(10,5), padx=20, ipadx=107)

tk.mainloop()
conn.close()