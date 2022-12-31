# Imports
import sqlite3


# Function to create/connect to database
def connect_db():
    try:
        # Create/connect to books database and create cursor object
        db_connect = sqlite3.connect('store_books.db')
        cursor = db_connect.cursor()

        # Create book table in db if it does not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT,
                            qty INTEGER)''')

        # Commit the changes to database
        db_connect.commit()

    except sqlite3.Error as e:
        # Handle the exception
        print('Something went wrong ⧱', e)
        exit()

    # Return cursor and db objects
    return cursor, db_connect
