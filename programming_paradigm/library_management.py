class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def check_in(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.check_in()
                return True
        return False

    def list_available_books(self):
        available_books = []
        for book in self._books:
            if book.is_available():
                available_books.append(book.title)
        return available_books
