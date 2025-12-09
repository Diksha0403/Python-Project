import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="diya1234")

mycursor = mydb.cursor()

#mycursor.execute("info")
mycursor.execute("Select * from info.employee")

for i in mycursor:
    print(i)


    