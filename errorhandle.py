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
    mycursor.execute("select e.name,e.age,d.deptname from employee e inner join departmet d on e.deptid=d.deptid where e.marks>60")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

except Error as e:
    print("something wrong please check your code:", e)
