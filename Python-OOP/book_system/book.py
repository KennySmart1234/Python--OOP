class Book:
    def __init__(self, book_id,  title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = True

    def borrow_book(self):
        self.isAvailable = False

    def return_book(self):
        self.isAvailable = True

    def is_available(self):
        return self.isAvailable

    def get_book_details(self):

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "isAvailable": self.isAvailable
        }

    def update_book(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn





