from tabulate import tabulate  # `pip install tabulate`
from functions import *


# Import demo data
def demo():

    while True:
        # Ask user to import demo data
        import_demo = input(
            "Welcome! \nDo you want to import demo data? \n⚠ Warning! Any existing records will be overwritten! \nEnter Yes/No to import demo data: ").lower()

        if import_demo == 'yes':
            # Call function to import demo
            demo_data()
            break

        elif import_demo == 'no':
            # Do nothing
            break

        else:
            print("\n⧱ Wrong input. Try again...\n")


# Main program
def main():

    while True:
        # Menu
        menu = input("""\nSelect one of the following options below:
        a - All Books
        e - Enter Book
        u - Update Book
        d - Delete Book
        s - Search Book
        q - Exit
        : """).lower()

        if menu == 'a':

            # Title
            print("\n▓ ALL BOOKS")

            # Call function to get all books
            all_books = get_book()

            # Display all books
            print_table(all_books)

        elif menu == 'e':

            # Title
            print("\n▓ ADD NEW BOOK\n")

            # Get inputs from user. Call func to get int input for qty
            title = input("Enter the book title: \n")
            author = input("Enter the book author: \n")
            qty = get_int_input("Enter the quantity in stock: \n")

            # Call function to add new book to db
            add_book(title, author, qty)

        elif menu == 'u':

            # Title
            print("\n▓ UPDATE BOOK\n")

            while True:
                # Get ID of book to edit from user
                book_id = get_int_input(
                    "Enter the ID of the book to edit or -1 to go back: \n")

                # Go back
                if book_id == -1:
                    break

                # Call function to search for the book
                to_edit = get_book('id', book_id)

                if to_edit:
                    # Check if any record with ID has been found
                    # Get the book title, author, quantity from search result
                    b_row = to_edit[0]
                    b_title, b_author, b_qty = b_row[1], b_row[2], b_row[3]

                    # Display book to edit
                    print_table(to_edit)

                    while True:
                        # Get attribut to edit from user
                        submenu = input("""\nSelect from the following options
                        t - Update Title
                        a - Update Author
                        q - Update Quantity
                        b - Back to main menu
                        : """).lower()

                        if submenu == 't':
                            # Get new title from user
                            b_title = input("Enter new book title: \n")

                            # Update record
                            update_book(book_id, b_title, b_author, b_qty)
                            break

                        elif submenu == 'a':
                            # Get new author from user
                            b_author = input("Enter new book author: \n")

                            # Update record
                            update_book(book_id, b_title, b_author, b_qty)
                            break

                        elif submenu == 'q':
                            # Get new quantity from user
                            b_qty = get_int_input(
                                "Enter new book quantity: \n")

                            # Update record
                            update_book(book_id, b_title, b_author, b_qty)
                            break

                        elif submenu == 'b':
                            # Do nothing and go back
                            break
                        else:
                            print("\n⧱ Wrong input. Try again...\n")

                    break

                else:
                    print("\n⧱ Oops! No record with that ID.\n")

        elif menu == 'd':
            # Title
            print("\n▓ DELETE BOOK\n")

            while True:
                # Get ID of book to delete from user
                delete_id = get_int_input(
                    "Enter the ID of the book to delete or -1 to go back: \n")

                # Call function to search for the book
                to_delete = get_book('id', delete_id)

                if delete_id == -1:
                    # Go back
                    break

                elif to_delete:

                    # Display book to delete
                    print_table(to_delete)

                    while True:
                        # Prompt user to delete record
                        delete_prompt = input(
                            "\nDo you want to delete this record? \nEnter Yes/No: ").lower()

                        if delete_prompt == 'yes':
                            # Delete the book
                            delete_book(delete_id)
                            break

                        elif delete_prompt == 'no':
                            # Do nothing/go back
                            break

                        else:
                            print("\n⧱ Wrong input. Try again...\n")

                else:
                    print("\n⧱ Oops! No record with that ID.\n")

        elif menu == 's':
            # Title
            print("\n▓ SEARCH FOR BOOK\n")

            while True:
                # Get attribut to edit from user
                search_menu = input("""Select from the following options
                id -    Search by ID
                ts -    Search by Title
                as -    Search by Author
                qs -    Search by Quantity
                b  -    Back to main menu
                : """).lower()

                if search_menu == 'id':
                    # Get the id
                    by_id = get_int_input("Enter the book ID to search: \n")

                    # Call function to search for the book
                    id_result = get_book('id', by_id)

                    # Display result
                    print_table(id_result)

                elif search_menu == 'ts':
                    # Get the title
                    by_title = input("Enter the book title to search: \n")

                    # Call function to search for the book
                    title_result = get_book('title', by_title)

                    # Display result
                    print_table(title_result)

                elif search_menu == 'as':
                    # Get the author
                    by_author = input("Enter the author to search: \n")

                    # Call function to search for the book
                    author_result = get_book('author', by_author)

                    # Display result
                    print_table(author_result)

                elif search_menu == 'qs':
                    # Get the quantity
                    by_qty = input("Enter the quantity to search: \n")

                    # Call function to search for the book
                    qty_result = get_book('qty', by_qty)

                    # Display result
                    print_table(qty_result)

                elif search_menu == 'b':
                    # Do nothing and go back
                    break

                else:
                    print("\n⧱ Wrong input. Try again...\n")

        elif menu == 'q':
            print("\n→ Good bye!\n")
            break

        else:
            print("\n⧱ Wrong input. Try again...\n")


# Check if user wants demo data
demo()

# Run main program
main()
