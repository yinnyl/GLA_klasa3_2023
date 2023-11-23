class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

book1 = Book("Potop", "Sienkiewicz", 1886, True)

class Library:
    def add_book(book):
        book.title = input("title: ")
        book.author = input("author: ")
        book.year = input("year: ")

    def display_books():
        book.draw()

    def borrow_book(title):
        book_to_borrow = input("borrow a book: ")

    def return_book(title):

library = Library()
display_books()