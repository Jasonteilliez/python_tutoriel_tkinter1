import mysql.connector
from mysql.connector import errorcode
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        pass

    def create_connection(self):
        return mysql.connector.connect(**DATABASE_CONFIG)
    
    def close_connection(self, db):
        try : 
            db.close()
        except mysql.connector.Error as err:
            self.mysql_error_handler(err) 

    def mysql_error_handler(self, error):
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        elif error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(error)






