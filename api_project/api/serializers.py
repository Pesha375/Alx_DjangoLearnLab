# serializers.py
from rest_framework import serializers # type: ignore
from .models import Book # type: ignore

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields in the Book model
