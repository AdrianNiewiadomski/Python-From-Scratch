class Book:
    def __init__(self, author, title, published_date):
        self.author = author
        self.title = title
        self.published_date = published_date

    def __repr__(self):
        return f"Book('{self.title}', {self.author}, {self.published_date}."
