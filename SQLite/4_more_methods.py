import sqlite3
from book import Book

in_memory_database_connection = sqlite3.connect(":memory:")
cursor = in_memory_database_connection.cursor()


def create_table():
    create_query = "CREATE TABLE books (author text, title text, published_date integer)"
    # Instead of having to remember to commit changes and close the connection, we can use a with clause:
    with in_memory_database_connection:
        cursor.execute(create_query)


def insert_book(book):
    with in_memory_database_connection:
        cursor.execute("INSERT INTO books VALUES (?, ?, ?)", book.to_tuple())


def get_books_by_author_name(author_name):
    # The select query does not have to be committed. Therefore, this method does not have the with clause.
    cursor.execute("SELECT * FROM books WHERE author=?", (author_name, ))
    return cursor.fetchall()


def get_all_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()


def update_published_date(book, published_date):
    with in_memory_database_connection:
        cursor.execute(
            """
                UPDATE books
                SET published_date = :published_date
                WHERE author = :author
                    AND title = :title
            """,
            {"author": book.author,
             "title": book.title,
             "published_date": published_date}
        )


def remove_book(book_title):
    with in_memory_database_connection:
        cursor.execute("DELETE from books WHERE title = ?", (book_title, ))


if __name__ == "__main__":
    create_table()

    insert_book(Book("Tolkien", "Hobbit", 2004))
    insert_book(Book("Rowling", "Harry Potter", 1997))
    insert_book(Book("Martin", "A Game of Thrones", 1996))
    insert_book(Book("Rothfuss", "The Name of the Wind", 2007))

    print("A book by Rowling is: ", get_books_by_author_name("Rowling"))
    print("All books are: ", get_all_books())

    update_published_date(Book("Rothfuss", "The Name of the Wind", 2007), 2008)
    print("All books are: ", get_all_books())

    remove_book("The Name of the Wind")
    print("All books are: ", get_all_books())

    in_memory_database_connection.close()
