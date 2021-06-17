class Book:
    def __init__(self, author, title, published_date):
        self.author = author
        self.title = title
        self.published_date = published_date

    def to_tuple(self):
        return self.author, self.title, self.published_date
