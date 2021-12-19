import sqlite3


def populate_database(cursor):
    cursor.execute("INSERT INTO books VALUES ('Tolkien', 'Hobbit', 2004)")


def read_from_table(cursor):
    cursor.execute("SELECT * FROM books WHERE author = 'Tolkien'")
    # You may get one row by calling the fetchone method.
    result = cursor.fetchone()
    # If no row meets the search condition, the fetchone method will return None.
    print("result: ", result)
    # To get more rows use cursor.fetchall(). This method returns a list.


def execute_query(fun):
    file_database_connection = sqlite3.connect("book.db")
    cursor = file_database_connection.cursor()

    fun(cursor)

    file_database_connection.commit()
    file_database_connection.close()


if __name__ == "__main__":
    # To insert rows to the database simply execute the INSERT INTO query.
    # execute_query(populate_database)
    execute_query(read_from_table)
