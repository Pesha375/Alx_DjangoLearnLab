from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    Fields:
        - name (CharField): The name of the author (max length: 100).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the author.
        """
        return self.name

class Book(models.Model):
    """
    Represents a book.
    Fields:
        - title (CharField): The title of the book (max length: 200).
        - publication_year (IntegerField): The year the book was published.
        - author (ForeignKey): The author of the book, linked to the Author model.
          Deleting an author deletes all their associated books.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        help_text="The author of this book."
    )

    def __str__(self):
        """
        Returns a string representation of the book's title.
        """
        return self.title
