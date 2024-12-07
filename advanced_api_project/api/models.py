from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    - name: The name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book.
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: The author of the book, linked to the Author model.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# Author model represents a book's author with a name field.
# Books are related to authors through a one-to-many relationship.



