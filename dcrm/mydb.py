import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Abhisek@1999'
    
)

#prepare a cursor object

cursorObject = database.cursor()

#creatr a database

cursorObject.execute("CREATE DATABASE Schwab")
print("All done database created YAYY!")