import mysql.connector
from mysql.connector import errorcode
from tables import TABLES
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.create_table()

    def create_connection(self):
        return mysql.connector.connect(**DATABASE_CONFIG)
    
    def mysql_error_handler(self, error):
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        elif error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(error)

    def create_table(self):
        try :
            db = self.create_connection()
            cursor = db.cursor()
            for table_name in TABLES:
                table_description = TABLES[table_name]
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)

    def customers_select_all(self):
        try :
            db = self.create_connection()
            cursor = db.cursor()
            query = "SELECT * FROM customers"
            cursor.execute(query)
            response = self.cursor.fetchall()
            return response
        except mysql.connector.Error as err:
            self.mysql_error_handler(err)



