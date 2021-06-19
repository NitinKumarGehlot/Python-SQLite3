import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()

#query the database
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Ku%'")
# c.execute("SELECT * FROM customers WHERE email LIKE '%com'")
# print(c.fetchone())
# c.fetchmany(3)

items=c.fetchall()
for i in items:
    print(i)


#commit our command
conn.commit()

#close connection
conn.close()
