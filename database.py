import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()

#create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    ) """)
#---or-----------
# c.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

#Datatypes---
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#commit our command
conn.commit()

#close connection
conn.close()

