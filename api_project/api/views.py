from django.shortcuts import render # type: ignore

# Create your views here.
from rest_framework import generics # type: ignore
from.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
