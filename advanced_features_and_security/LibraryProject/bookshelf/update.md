# update.md

# Command to update the title of “1984” to “Nineteen Eighty-Four”
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book  # Expected output: <Book: Nineteen Eighty-Four by George Orwell>
