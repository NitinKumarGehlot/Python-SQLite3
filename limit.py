import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()


#query the database  -LIMIT
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
c.execute("SELECT rowid, * FROM customers LIMIT 2")

# print(c.fetchone())
# c.fetchmany(3)

items=c.fetchall()
for i in items:
    print(i)



#close connection
conn.close()
