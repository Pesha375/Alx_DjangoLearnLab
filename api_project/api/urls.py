from django.urls import path, include
from rest_framework.authtoken import views as auth_views # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import BookViewSet, BookList

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router

    # Token retrieval endpoint
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
]


