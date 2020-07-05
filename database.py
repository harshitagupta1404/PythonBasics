import mysql.connector as db
"""
# connect method will give us database connection
mydb = db.connect(host="localhost", user="root", passwd="root")
# cursor is like an object
myCursor = mydb.cursor()
# execute is used to execute any sql query, in execute function we'll write the sql query that we want to execute
myCursor.execute("show databases")
for i in myCursor:
    print(i)
"""
# if u want to execute query on specific table, then you need to connect to database schema also
mydb = db.connect(host="localhost", user="root", passwd="root", database="practice")
myCursor = mydb.cursor()
myCursor.execute("select * from student")
"""for i in myCursor:
    print(i)"""
# fetchall is used to fetch all records
"""res = myCursor.fetchall()
for i in res:
    print(i)"""
# we can use fetchone to fetch one record
res = myCursor.fetchone()
for i in res:
    print(i)