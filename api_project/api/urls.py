# api/urls.py
from django.urls import path # type: ignore
from .views import BookList # type: ignore

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
