import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Formulae20!",
    database="dummy"
)

mycursor=mydb.cursor()
mycursor.execute("select avg(marks),name from employee group by name having avg(marks)>90")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)
