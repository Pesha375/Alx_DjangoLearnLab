from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import BookViewSet, BookList
from django.urls import path # type: ignore
from .views import BookList # type: ignore


# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
     # Route for the simple list view
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router-generated URLs for the ViewSet
    path('', include(router.urls)),
    
    
]



