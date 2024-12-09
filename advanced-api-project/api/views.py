from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from rest_framework.filters import filters.OrderingFilter



# List all books with advanced filtering, searching, and ordering
class BookListView(generics.ListCreateAPIView):
    """
    API view to retrieve the list of books with advanced query capabilities:
    - Filtering by title, author, and publication year.
    - Searching in title and author fields.
    - Ordering by title and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Public access for read-only; authenticated users can create
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields available for filtering
    search_fields = ['title', 'author']  # Fields available for searching
    ordering_fields = ['title', 'publication_year']  # Fields available for ordering
    ordering = ['title']  # Default ordering by title

    def perform_create(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)


# Retrieve, update, or delete a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Public read-only; owner can update/delete

    def perform_update(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)


# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Only authenticated users and owners can update

    def perform_update(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Only authenticated users and owners can delete

    
    
