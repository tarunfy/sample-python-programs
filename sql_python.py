import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database = "test")

mycursor = mydb.cursor()

mycursor.execute("select * from user")


result = mycursor.fetchone()

for i in result:
    print(i,end=' ')