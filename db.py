import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE ZSCALER_VERSIONS
         (ID INT PRIMARY KEY     NOT NULL,
         VERSION TEXT NOT NULL,
         REMARKS TEXT);''')

print("Table created successfully")

conn.close()