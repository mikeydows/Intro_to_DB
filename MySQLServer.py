import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without selecting a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # change to your MySQL username
            password="your_password"  # change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists (this prevents failure if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection properly
        try:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
                # print("MySQL connection is closed")
        except:
            pass

if __name__ == "__main__":
    create_database()
