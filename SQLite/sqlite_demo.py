import sqlite3


def create_database():
    # in_memory_database_connection = sqlite3.connect(":memory:")

    file_database_connection = sqlite3.connect("book.db")
    # If you run this script after adding the line above the file "book.db" will be created.

    # To execute SQL queries, we have to create a cursor.
    cursor = file_database_connection.cursor()

    # You may place your queries in docstring to increase the readability:
    create_query = """
        CREATE TABLE books (
            author text,
            title text,
            published_date text
        )
    """
    cursor.execute(create_query)

    # To actually complete the execution of the query you have to commit it.
    file_database_connection.commit()

    # It is a good practice to close the connection after your work with the database is done.
    file_database_connection.close()


if __name__ == "__main__":
    # sqlite3.OperationalError: table books already exists
    create_database()
