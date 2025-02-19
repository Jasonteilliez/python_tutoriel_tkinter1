import tkinter as tk
from tkinter import ttk
from customers import CustomersModel

class DisplayLineFrame(tk.Frame):
    def __init__(self, parent, update_customer, data):
        super().__init__(parent)
        self.update_customer = update_customer
        self.data = data
        self.widget_list=[]
        self.display_data()

    def display_data(self):
        button_edit = tk.Button(self, text="Edit", command=self.click_edit)
        button_edit.grid(row=0, column=0)
        self.widget_list.append(button_edit)

        for key, value in enumerate(self.data):
            label_data = tk.Label(self, text=value)
            label_data.grid(row=0,column=key+1)
            self.widget_list.append(label_data)

    def display_edit(self):
        button_valider = tk.Button(self, text="Valider", command=self.click_valider)
        button_annuler = tk.Button(self, text="Annuler", command=self.click_annuler)
        button_valider.grid(row=0, column=0)
        button_annuler.grid(row=0, column=1)
        self.widget_list.append(button_valider)
        self.widget_list.append(button_annuler)

        label_first_name = tk.Label(self, text="First Name :")
        label_last_name = tk.Label(self, text="Last Name :")
        label_zipcode = tk.Label(self, text="Zipcode :")
        label_price_paid = tk.Label(self, text="Price Paid :")
        label_user_id = tk.Label(self, text="Customer ID :")

        label_first_name.grid(row=0, column=2, sticky="w")
        label_last_name.grid(row=0, column=4, sticky="w")
        label_zipcode.grid(row=0, column=6, sticky="w")
        label_price_paid.grid(row=0, column=8, sticky="w")
        label_user_id.grid(row=0, column=10, sticky="w")

        self.widget_list.append(label_first_name)
        self.widget_list.append(label_last_name)
        self.widget_list.append(label_zipcode)
        self.widget_list.append(label_price_paid)
        self.widget_list.append(label_user_id)

        self.entry_first_name = tk.Entry(self)
        self.entry_last_name = tk.Entry(self)
        self.entry_zipcode = tk.Entry(self)
        self.entry_price_paid = tk.Entry(self)
        self.entry_user_id = tk.Entry(self)

        self.entry_first_name.insert('end', self.data[0])
        self.entry_last_name.insert('end', self.data[1])
        self.entry_zipcode.insert('end', self.data[2])
        self.entry_price_paid.insert('end', self.data[3])
        self.entry_user_id.insert('end', self.data[4])

        self.entry_user_id.config(state="readonly")

        self.entry_first_name.grid(row=0, column=3, sticky="e", pady=5)
        self.entry_last_name.grid(row=0, column=5, sticky="e", pady=5)
        self.entry_zipcode.grid(row=0, column=7, sticky="e", pady=5)
        self.entry_price_paid.grid(row=0, column=9, sticky="e", pady=5)
        self.entry_user_id.grid(row=0, column=11, sticky="e", pady=5)

        self.widget_list.append(self.entry_first_name)
        self.widget_list.append(self.entry_last_name)
        self.widget_list.append(self.entry_zipcode)
        self.widget_list.append(self.entry_price_paid)
        self.widget_list.append(self.entry_user_id)
    
    def click_edit(self):
        self.reset_widget()
        self.display_edit()

    def click_annuler(self):
        self.reset_widget()
        self.display_data()

    def click_valider(self):
        data = self.get_data()
        self.update_customer(data)

    def reset_widget(self):
        for widget in self.widget_list:
            widget.destroy()
        self.widget_list=[]

    def get_data(self):
        return {
            "first_name": self.entry_first_name.get(),
            "last_name": self.entry_last_name.get(),
            "zipcode": self.entry_zipcode.get(),
            "price_paid": self.entry_price_paid.get(),
            "user_id": self.data[4]
        }
        

class SearchWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Search Customers")

        self.customers_db = CustomersModel()

        self.customers = []
        self.customers_list = []

        self.search_option_list = ["Cutomer ID", "First Name", "Last Name", "Zipcode"]
        self.search_option_dict ={
            "Cutomer ID":"user_id",
            "First Name":"first_name",
            "Last Name":"last_name",
            "Zipcode":"zipcode"
        }

        self.search_option = tk.StringVar()
        self.search_option.set(self.search_option_list[0])

        self.init_ui()
        
    def init_ui(self):
        # Create widget
        self.frame_title = tk.Frame(self)
        self.frame_title.grid_columnconfigure(0, weight=1)
        self.frame_title.grid_rowconfigure(0, weight=1)
        self.frame_search = tk.Frame(self)
        self.frame_display = tk.Frame(self)

        label_title = tk.Label(self.frame_title, text="SEARCH CUSTOMERS")
        label_search = tk.Label(self.frame_search, text="Search by :")
        label_result_title = tk.Label(self.frame_search, text="Result :")
        self.label_not_found = tk.Label(self.frame_display, text="Record_not found...")

        self.entry_search = tk.Entry(self.frame_search)

        button_search = tk.Button(self.frame_search, text="Search", command=self.display_search_customers)

        dropmenu_search = ttk.Combobox(self.frame_search, textvariable=self.search_option, values=self.search_option_list, state="readonly")

        # Display widget
        self.frame_title.pack(expand=False, fill='x', padx=10, pady=5)
        label_title.grid(row=0, column=0, sticky="nsew")

        self.frame_search.pack(expand=False, fill='x', padx=10, pady=5)
        label_search.grid(row=0, column=0, sticky='w')
        dropmenu_search.grid(row=0, column=1)
        self.entry_search.grid(row=0, column=2, sticky='w', padx=(10,0))
        button_search.grid(row=1, column=0, columnspan=2, sticky='w', pady=(10,10))
        label_result_title.grid(row=2,column=0, columnspan=2, sticky='w')

        self.frame_display.pack(expand=False, fill='x', padx=10, pady=5)

    def fetch_customers_by_search(self):
        print ("\nFetch customers.")
        data={
            "column":self.search_option_dict[self.search_option.get()],
            "value":self.entry_search.get()
        }
        return self.customers_db.get_customer_by(data)

    def update_cutomer(self, values): 
        print("\nUpdate customer :\n"\
        "   First Name : {first_name}\n"\
        "   Last Name : {last_name}\n"\
        "   Zipcode : {zipcode}\n"\
        "   Price paid : {price_paid}\n"\
        "   Customer ID : {user_id}"\
        .format(**values))

        self.customers_db.update_customer(values)
        self.display_search_customers()

    def display_search_customers(self):
        if self.customers_list:
            for c in self.customers_list:
                c.destroy()

        self.customers_list = []
        self.customers = self.fetch_customers_by_search()

        if self.customers:
            for key, customer in enumerate(self.customers):
                display_line_frame = DisplayLineFrame(self.frame_display, self.update_cutomer, customer)
                display_line_frame.grid(row=key, column=0)
                self.customers_list.append(display_line_frame)