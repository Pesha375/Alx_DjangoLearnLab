from django.shortcuts import render # type: ignore
from rest_framework.permissions import IsAuthenticated, IsAdminUser # type: ignore
from rest_framework.permissions import BasePermission # type: ignore
from rest_framework import viewsets # type: ignore
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
    
    