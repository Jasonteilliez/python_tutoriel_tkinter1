import tkinter as tk
from customers import CustomersModel
        

class MainFrame(tk.Frame):
    def __init__(self, parent, add_customer, fetch_all_customers):
        super().__init__(parent)
        self.add_customer = add_customer
        self.fetch_all_customers = fetch_all_customers

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

        button_add_customer = tk.Button(self, text="submit", command=self.add_customer)
        button_clear_field = tk.Button(self, text="clear", command=self.clear_field)
        button_fetch_all_customers = tk.Button(self, text="Curtomers list", command=self.display_customers_list)
        
        # Display widget
        label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        label_first_name.grid(row=1, column=0, padx=5, sticky="w")
        label_last_name.grid(row=2, column=0, padx=5, sticky="w")
        label_zipcode.grid(row=3, column=0, padx=5, sticky="w")
        label_price_paid.grid(row=4, column=0, padx=5, sticky="w")

        self.entry_first_name.grid(row=1, column=1, sticky="e", pady=5)
        self.entry_last_name.grid(row=2, column=1, sticky="e", pady=5)
        self.entry_zipcode.grid(row=3, column=1, sticky="e", pady=5)
        self.entry_price_paid.grid(row=4, column=1, sticky="e", pady=5)

        button_add_customer.grid(row=5,column=0, sticky="w", padx=5, pady=5)
        button_clear_field.grid(row=5,column=1, padx=5, pady=5)
        button_fetch_all_customers.grid(row=6,column=0, padx=5, pady=5)

        self.frame_display_customers.grid(row=7, column=0, columnspan=2, sticky='w')

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
        self.label_customers_list = []
        self.customers = self.fetch_all_customers()

        if self.customers:
            for k_customer, customer in enumerate(self.customers):
                label_data_list = []
                for k_data, data in enumerate(customer):
                    label_data = tk.Label(self.frame_display_customers, text=data)
                    label_data_list.append(label_data)
                    label_data.grid(row=k_customer, column=k_data, padx=5, sticky='w')
                self.label_customers_list.append(label_data_list)
            print(self.label_customers_list)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tutorial Step 16 : Customer Relationship Management")
        self.root.iconbitmap('Cours/assets/holo_icon.ico')
        self.root.geometry("400x400")

        self.customers_db = CustomersModel()

        self.main_frame = MainFrame(root, self.add_customer, self.fetch_all_customers)
        self.main_frame.pack(expand=True, fill='both')
        
    def add_customer(self):
        values = self.main_frame.get_data()

        print("\nAdd customer :\n"\
        "   First Name : {first_name}\n"\
        "   Last Name : {last_name}\n"\
        "   Zipcode : {zipcode}\n"\
        "   Price paid : {price_paid}"\
        .format(**values))
        
        self.customers_db.create(values)
        self.main_frame.clear_field()

    def fetch_all_customers(self):
        print ("\nFetch all customers.")
        return self.customers_db.select_all()