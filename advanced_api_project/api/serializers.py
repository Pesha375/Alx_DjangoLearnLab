from rest_framework import serializers
from .models import Author, Book # type: ignore


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Validates:
        - The publication year must not be in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensures the publication year is not in the future.
        """
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:  # Fixed the incorrect '&gt;' syntax
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes:
        - A nested BookSerializer to serialize related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
