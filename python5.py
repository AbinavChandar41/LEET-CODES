import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Formulae20!",
        database="dummy"
    )

    mycursor = mydb.cursor()
    mycursor.execute("select count(name),departmet.deptname from employee inner join departmet on employee.deptid=departmet.deptid group by deptname")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

except Error as e:
    print("something wrong please check your code:", e)
