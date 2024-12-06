from django.shortcuts import render # type: ignore
from rest_framework.viewsets import ModelViewSet # type: ignore

from rest_framework import generics # type: ignore
from.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


