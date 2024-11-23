from django.urls import path
from .views import list_books, LibraryDetailView
from relationship_app import views # type: ignore

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
     path('library/<int:library_id>/', views.library_detail, name='library_detail'), # Class-based view
]
