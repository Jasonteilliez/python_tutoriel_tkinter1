import mysql.connector
from database import Database
from tables import CUSTOMERS_MODEL


class CustomersModel (Database):
    def __init__(self):

        super().__init__()
        self.create_table()

    def create_table(self):
        try :
            db = self.create_connection()
            cursor = db.cursor()
            print("Creating table Customers.")
            cursor.execute(CUSTOMERS_MODEL)
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)
        self.close_connection(db)

    def get_all_customers(self):
        try :
            db = self.create_connection()
            cursor = db.cursor()
            query = "SELECT * FROM customers"
            cursor.execute(query)
            response = cursor.fetchall()
            self.close_connection(db)
            return response
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)
        self.close_connection(db)

    def get_customer_by(self, data):
        try:
            db = self.create_connection()
            cursor = db.cursor()
            query = "SELECT * FROM customers WHERE {} = %s".format(data['column'])
            cursor.execute(query, (data['value'],))
            response = cursor.fetchall()
            self.close_connection(db)
            return response
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)
        self.close_connection(db)

    def create_customer(self, values):
        try:
            db = self.create_connection()
            cursor = db.cursor()
            query = """INSERT INTO customers (first_name, last_name, zipcode, price_paid)
                VALUES (%(first_name)s, %(last_name)s, %(zipcode)s, %(price_paid)s)"""
            cursor.execute(query, values)
            db.commit()
            self.close_connection(db)
            return
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)
        self.close_connection(db)

    def update_customer(self, values):
        try:
            db = self.create_connection()
            cursor = db.cursor()
            query = """
                UPDATE customers SET 
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                zipcode = %(zipcode)s,
                price_paid = %(price_paid)s
                WHERE user_id = %(user_id)s
            """
            cursor.execute(query, values)
            db.commit()
            self.close_connection(db)
            return
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)
        self.close_connection(db)