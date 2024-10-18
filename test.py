import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
      host="localhost",          # Your MySQL host
      user="root",               # Your MySQL username
      password="SUDHIR",         # Your MySQL password
      database="PythonSqlTest",  # Replace with your database name
      auth_plugin='mysql_native_password'  # Specify the auth plugin here
    )

    if mydb.is_connected():
        print("Connection Successful")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if mydb.is_connected():
        mydb.close()
