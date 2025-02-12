TABLES = {}
TABLES['customers'] = ("""
    CREATE TABLE IF NOT EXISTS customers (
	    first_name VARCHAR(255),
	    last_name VARCHAR(255),
	    zipcode INT(10),
	    price_paid DECIMAL(10,2),
	    user_id INT AUTO_INCREMENT,
        PRIMARY KEY (user_id)
    )
""")