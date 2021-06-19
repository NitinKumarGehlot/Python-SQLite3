import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()

#query the database
c.execute("SELECT rowid, * FROM customers")
# print(c.fetchone())
# c.fetchmany(3)

items=c.fetchall()
for i in items:
    print(i)


#commit our command
conn.commit()

#close connection
conn.close()
