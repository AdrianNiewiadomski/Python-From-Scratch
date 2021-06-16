import sqlite3
from book import Book


def populate_database_question_marks(cursor, **kwargs):
    book = kwargs['book']

    # The approach shown below while tempting it is vulnerable to attacks (SQL injection).
    # Therefore it is considered a bad practice.
    # cursor.execute("INSERT INTO books VALUES ('{}', '{}', {})".format(book.author, book.title, book.published_date))

    # We can use a DB-API’s parameter substitution. As a placeholder we use "?" sign and then provide a tuple of values:
    cursor.execute("INSERT INTO books VALUES (?, ?, ?)", (book.author, book.title, book.published_date))


def populate_database_named_placeholders(cursor, **kwargs):
    book = kwargs['book']
    # Or, we can use named placeholders:
    cursor.execute("INSERT INTO books VALUES (:author, :title, :year)",
                   {"author": book.author, "title": book.title, "year": book.published_date})


def read_from_table(cursor, **kwargs):
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    print("result: ", result)


def execute_query(fun, **kwargs):
    file_database_connection = sqlite3.connect("book.db")
    cursor = file_database_connection.cursor()

    fun(cursor, **kwargs)

    file_database_connection.commit()
    file_database_connection.close()


if __name__ == "__main__":
    book_1 = Book("Rowling", "Harry Potter", 1997)
    book_2 = Book("Martin", "A Game of Thrones", 1996)

    # execute_query(populate_database_question_marks, book=book_1)
    # execute_query(populate_database_named_placeholders, book=book_2)
    execute_query(read_from_table)
