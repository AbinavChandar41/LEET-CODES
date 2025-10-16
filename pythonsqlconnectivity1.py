import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Formulae20!",
    database="dummy"
)

mycursor=mydb.cursor()
mycursor.execute("select e.name,d.deptname from employee e right join departmet d on e.deptid=d.deptid ")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)
