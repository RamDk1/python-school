class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

class LibraryCatalog:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def display_catalog(self):
        for book in self.catalog:
            print(f'Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Year: {book.publication_year}')

    def change_genre_book(self, title, new_genre):
        for book in self.catalog:
            if book.title == title:
                book.genre = new_genre
            print(f"Genre of '{title}' changed to '{new_genre}'")
            return
        print(f"Book with title '{title}' not found")

# Example usage
library = LibraryCatalog()
library.add_book(Book("1984", "George Orwell", "Dystopian", 1949))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960))

print("Before changing genre:")
# Display the catalog
library.display_catalog()

library.change_genre_book("1984", "Science Fiction")

print("\nAfter changing genre")
library.display_catalog()
