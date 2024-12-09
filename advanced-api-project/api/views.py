from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .permissions import IsOwnerOrReadOnly

# Author views
class AuthorList(generics.ListCreateAPIView):
    """
    List all authors or create a new author.
    - GET: List all authors.
    - POST: Create a new author. Requires authentication for creation.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an author.
    - GET: Retrieve an author by ID.
    - PUT: Update an author by ID. Requires authentication.
    - DELETE: Delete an author by ID. Requires authentication.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Book views
class BookList(generics.ListAPIView):
    """
    List all books.
    - GET: List all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetail(generics.RetrieveAPIView):
    """
    Retrieve a book.
    - GET: Retrieve a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    - POST: Create a new book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    - PUT: Update a book by ID. Requires authentication and ownership.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    - DELETE: Delete a book by ID. Requires authentication and ownership.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]