import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()

#query the database
c.execute("SELECT * FROM customers")
# print(c.fetchone())
# c.fetchmany(3)

items=c.fetchall()

print("NAME " +"\t\tEMAIL")
print("-----" +"\t\t-----")
for i in items:
    print(i[0] + " " + i[1] + "\t" + i[2])

#commit our command
conn.commit()

#close connection
conn.close()

