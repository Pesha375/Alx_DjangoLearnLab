from relationship_app.models import Book, Author, Library, Librarian

def query_books_by_author(author_name):
    """
    Query and list all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        if books.exists():
            print(f"Books by {author_name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for author '{author_name}'.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

def query_books_in_library(library_name):
    """
    List all books available in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        if books.exists():
            print(f"Books in library '{library_name}':")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found in the library '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

def query_librarian_for_library(library_name):
    """
    Retrieve the librarian responsible for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Access the OneToOneField directly
        if librarian:
            print(f"Librarian for library '{library_name}': {librarian.name}")
        else:
            print(f"No librarian assigned to the library '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'.")

# Example Usage
query_books_by_author('Author Name')
query_books_in_library('Library Name')
query_librarian_for_library('Library Name')
