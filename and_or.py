import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()


#query the database  -AND/OR
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Ku%' OR rowid=5")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Ku%' AND rowid=7")

# print(c.fetchone())
# c.fetchmany(3)

items=c.fetchall()
for i in items:
    print(i)



#close connection
conn.close()
