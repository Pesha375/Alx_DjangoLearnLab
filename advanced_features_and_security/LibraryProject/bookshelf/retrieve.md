# retrieve.md

# Command to retrieve and display all attributes of the book created
from bookshelf.models import Book
# Retrieve the book

```python
book = Book.objects.get(title='1984')
print(book.title, book.author, book.publication_year)