from django.urls import path
from .views import list_books, LibraryDetailView
from relationship_app import views # type: ignore

from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
