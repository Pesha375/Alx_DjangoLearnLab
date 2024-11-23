from relationship_app.models import Book, Author, Library, Librarian

def query_books_by_author(author_name):
    # Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books = author.book_set.all()
    for book in books:
        print(book.title)

def query_books_in_library(library_name):
    # List all books in a library
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

def query_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(librarian.name)

# Usage
query_books_by_author('Author Name')
query_books_in_library('Library Name')
query_librarian_for_library('Library Name')