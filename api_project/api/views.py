from django.shortcuts import render # type: ignore

# Create your views here.
# views.py
from rest_framework.generics import ListAPIView # type: ignore
from.models import Book
from.serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
