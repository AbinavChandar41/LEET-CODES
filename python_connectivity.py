import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Formulae20!",
    database="dummy"
)

mycursor=mydb.cursor()
mycursor.execute("select count(name) from employee where marks=67;")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)
