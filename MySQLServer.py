#!/usr/bin/python3
"""
Script to create a database 'alx_book_store' in MySQL server.
"""

import mysql.connector

def create_database():
    connection = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # replace with your MySQL username
            password="password"  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
