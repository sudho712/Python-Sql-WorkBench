import mysql.connector

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',  # Default XAMPP MySQL username
    'password': '',  # Default XAMPP MySQL password (usually empty)
    'database': 'test'  # Replace with your database name
}

try:
    # Establish connection
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        print("Connected to MySQL database!")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Example query: Insert a new user
        cursor.execute("INSERT INTO test (id, name) VALUES (%s, %s)", (1, 'John Doe'))
        connection.commit()  # Save changes
        print("Data inserted successfully!")

        # Example query: Fetch data
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()
        for row in results:
            print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
