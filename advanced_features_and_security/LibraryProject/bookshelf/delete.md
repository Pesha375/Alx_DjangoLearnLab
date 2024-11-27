# delete.md

# Command to delete the book instance
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by checking for any remaining books
Book.objects.all()  # Expected output: <QuerySet []>
