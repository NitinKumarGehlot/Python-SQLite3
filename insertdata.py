import sqlite3

# conn=sqlite3.connect(":memory:")
conn=sqlite3.connect("customer.db")

#create cursor
c=conn.cursor()

#insert data--------


#if input many entry at a time 
# many_customers=[
#                     ('seema','Arya','seema433@gmail.com'),
#                     ('Tikendra','Kumar','tikend@gmail.com'),
#                     ('Ashutosh','Kumar','ashu@tosh.com')
#                 ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

#one by one entry
c.execute("INSERT INTO customers VALUES ('Kamnee','Devi','kamnee@gmail.com')")



print("command executed succesfully")
#commit our command
conn.commit()

#close connection
conn.close()
