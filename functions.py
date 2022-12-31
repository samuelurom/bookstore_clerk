# Imports
import sqlite3
from config import connect_db
from tabulate import tabulate


# Function to print error message
def error(er):
    # Handle the exception
    print('Something went wrong ⧱', er, '\n')


# Function to add new books to database, b_id has a default falsy value
def add_book(b_title, b_author, b_qty, b_id=''):

    # Connect to db and grab the db and cursor objects
    cursor, db = connect_db()

    try:
        if b_id:
            # Ordered list of fields in record
            record = (b_id, b_title, b_author, b_qty)

            # Execute command to insert record to book table in db
            cursor.execute('''INSERT INTO book (id, title, author, qty)
                                VALUES (?, ?, ?, ?)''', record)

        else:
            # Ordered list of fields in record
            record = (b_title, b_author, b_qty)

            # Execute command to insert record to book table in db
            cursor.execute('''INSERT INTO book (title, author, qty)
                                VALUES (?, ?, ?)''', record)

        # Commit changes to db
        db.commit()

        # Feedback
        print('Record inserted ✔')

    except sqlite3.Error as e:
        error(e)

    finally:
        # Close the db connection
        db.close()


# Function to update book information
def update_book(b_id, b_title, b_author, b_qty):

    # Ordered list of fields in record
    updated_record = (b_title, b_author, b_qty, b_id)

    # Connect to db and grab the db and cursor objects
    cursor, db = connect_db()

    try:
        # Execute command to update record in book table
        cursor.execute('''UPDATE book
                            SET title = ?, author = ?, qty = ?
                            WHERE id = ?''', updated_record)

        # Commit changes to db
        db.commit()

        # Feedback
        print('Record updated ✔\n')

    except sqlite3.Error as e:
        error(e)

    finally:
        # Rollback changes and close the db connection
        db.rollback()
        db.close()


# Function to delete book from db
def delete_book(b_id):

    # Connect to db and grab the db and cursor objects
    cursor, db = connect_db()

    try:
        # Execute command to delete record from table
        cursor.execute('DELETE FROM book WHERE id = ?', (b_id,))

        # Commit changes to db
        db.commit()

        # Feedback
        print('Record deleted ✔\n')

    except sqlite3.Error as e:
        error(e)

    finally:
        # Rollback changes and close the db connection
        db.rollback()
        db.close()


# Function to get all books from db or search db for specific book based on criteria
# Parameters have default falsy values
def get_book(search_by='', search_term=''):

    # Connect to db and grab the db and cursor objects
    cursor, db = connect_db()

    # Initialise list to store result
    result = []

    try:
        if search_by and search_term:
            # Execute command to select records based on search criteria
            # COLLATE NOCASE ensures case is insensitive when comparing strings
            cursor.execute(
                '''SELECT * FROM book WHERE {} = ? COLLATE NOCASE'''.format(search_by), (search_term,))

            # Fetch the result from query
            result = cursor.fetchall()

        else:
            # Execute command to select all records
            cursor.execute('SELECT * FROM book')

            # Fetch the result from query
            result = cursor.fetchall()

    except sqlite3.Error as e:
        error(e)

    finally:
        # Close the db connection
        db.close()

    # return the data
    return result


# Function to populate book table with demo data
def demo_data():

    # Connect to db and grab the db and cursor objects
    cursor, db = connect_db()

    # Delete book table
    cursor.execute('DROP table book')
    db.close()

    # Demo data
    data = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 40),
        (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12),
        (3006, "To Kill a Mockingbird", "Harper Lee", 7),
        (3007, "Nineteen Eighty Four", "George Orwell", 22),
        (3008, "Designing Data-Intensive Applications", "Martin Kleppmann", 6),
        (3009, "Eloquent JavaScript, 3rd Edition", "Marijn Haverbeke", 12),
        (3010, "Mastery", "Robert Greene", 35)
    ]

    # Insert each row in list to db using add_book() func
    for row in data:
        add_book(row[1], row[2], row[3], row[0])

    # Feedback
    print('\nDemo data imported ✔\n')


# Function to get integer input from user, using try and except blocks to check for valid inputs
def get_int_input(prompt):

    while True:
        try:
            value = int(input(prompt))
            return value

        except (TypeError, ValueError):
            print("\n⧱ Wrong input! Integer expected. Try again...\n")


# Function to print 2D list in table format
def print_table(book_list):
    # Create the books table
    books_table = tabulate(book_list, headers=[
        "ID", "Title", "Author", "Qty"])

    if book_list:
        # Print the formated table if list not empty
        print('\n', books_table, '\n')
    else:
        print('\n⧱ Oops! No record matches the search term.\n')
