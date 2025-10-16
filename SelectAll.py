import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Formulae20!",
    database="dummy"
)
mycursor=mydb.cursor()
mycursor.execute("select * from employee")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

