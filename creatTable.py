import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUDHIR", 
)

mycursor = mydb.cursor()

