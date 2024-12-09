from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

# List all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Public access for read-only, authenticated users can create

    def perform_create(self, serializer):
        # Save the book with the authenticated user as the owner
        serializer.save(owner=self.request.user)

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Public read-only, owner can update/delete

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
    
    
