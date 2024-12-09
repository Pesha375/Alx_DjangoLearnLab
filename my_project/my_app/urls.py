pythonCopy codefrom django.urls import path # type: ignore
from .views import BookListCreateAPIView # type: ignore

urlpatterns = [
    path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"), # type: ignore
]





