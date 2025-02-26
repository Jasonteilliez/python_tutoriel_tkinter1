import tkinter as tk
import csv

from customers import CustomersModel
from search_window import SearchWindow

        
class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padx=10)
        self.controller = controller

        self.customers = []
        self.label_customers_list = []

        self.init_ui()

    def init_ui(self):
        # Create widget
        self.frame_display_customers = tk.Frame(self)

        label_title = tk.Label(self, text="Main Frame")

        label_first_name = tk.Label(self, text="First Name")
        label_last_name = tk.Label(self, text="Last Name")
        label_zipcode = tk.Label(self, text="Zipcode")
        label_price_paid = tk.Label(self, text="Price Paid")

        self.entry_first_name = tk.Entry(self)
        self.entry_last_name = tk.Entry(self)
        self.entry_zipcode = tk.Entry(self)
        self.entry_price_paid = tk.Entry(self)

        button_add_customer = tk.Button(self, text="submit", command=self.controller.add_customer)
        button_clear_field = tk.Button(self, text="clear", command=self.clear_field)
        button_fetch_all_customers = tk.Button(self, text="Curtomers list", command=self.display_customers_list)
        button_csv_export = tk.Button(self, text="Save to CSV", command=self.controller.export_customer_data_to_csv)
        button_search_customers = tk.Button(self, text="Search Customers", command=self.open_search_window)
        
        # Display widget
        label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        label_first_name.grid(row=1, column=0, sticky="w")
        label_last_name.grid(row=2, column=0, sticky="w")
        label_zipcode.grid(row=3, column=0, sticky="w")
        label_price_paid.grid(row=4, column=0, sticky="w")

        self.entry_first_name.grid(row=1, column=1, sticky="e", pady=5)
        self.entry_last_name.grid(row=2, column=1, sticky="e", pady=5)
        self.entry_zipcode.grid(row=3, column=1, sticky="e", pady=5)
        self.entry_price_paid.grid(row=4, column=1, sticky="e", pady=5)

        button_add_customer.grid(row=5,column=0, sticky="w", pady=5)
        button_clear_field.grid(row=5,column=1, pady=5)
        button_fetch_all_customers.grid(row=6,column=0, pady=5)

        self.frame_display_customers.grid(row=7, column=0, columnspan=2, sticky='w')

        button_csv_export.grid(row=8, column=0 , stick='w')
        button_search_customers.grid(row=8, column=1, sticky='w')

    def clear_field(self):
        print("\nClear customer creation fields.")
        self.entry_first_name.delete(0, "end")
        self.entry_last_name.delete(0, "end")
        self.entry_zipcode.delete(0, "end")
        self.entry_price_paid.delete(0, "end")

    def get_data(self):
        return {
            "first_name": self.entry_first_name.get(),
            "last_name": self.entry_last_name.get(),
            "zipcode": self.entry_zipcode.get(),
            "price_paid": self.entry_price_paid.get(),
        }

    def display_customers_list(self): 
        if self.label_customers_list:
            for labels in self.label_customers_list:
                for label in labels:
                    label.destroy() 
        self.label_customers_list = []

        self.customers = self.controller.fetch_all_customers()

        if self.customers:
            for k_customer, customer in enumerate(self.customers):
                label_data_list = []
                for k_data, data in enumerate(customer):
                    label_data = tk.Label(self.frame_display_customers, text=data)
                    label_data_list.append(label_data)
                    label_data.grid(row=k_customer, column=k_data, sticky='w')
                self.label_customers_list.append(label_data_list)

    def open_search_window(self):
        SearchWindow(self)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tutorial Step 16 : Customer Relationship Management")
        self.root.iconbitmap('Cours/assets/holo_icon.ico')
        self.root.geometry("400x400")

        self.customers_db = CustomersModel()

        self.main_frame = MainFrame(root, self)
        self.main_frame.pack(expand=True, fill='both')
        
    def add_customer(self):
        values = self.main_frame.get_data()

        print("\nAdd customer :\n"\
        "   First Name : {first_name}\n"\
        "   Last Name : {last_name}\n"\
        "   Zipcode : {zipcode}\n"\
        "   Price paid : {price_paid}"\
        .format(**values))
        
        self.customers_db.create_customer(values)
        self.main_frame.clear_field()

    def fetch_all_customers(self):
        print ("\nFetch all customers.")
        return self.customers_db.get_all_customers()
    
    def export_customer_data_to_csv(self):
        print ("\nExporting data.....")
        customers_data = self.fetch_all_customers()

        try: 
            with open('Cours/16_CRM/data/customers.csv', 'a+', newline='') as f:
                f.truncate(0)
                w = csv.writer(f, dialect='excel')
                w.writerows(customers_data)
                print ("\nData Exported.")
        except :
            print ("Failed to export data.")
        

