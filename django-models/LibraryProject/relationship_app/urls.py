from django.urls import path
from .views import list_books, LibraryDetailView
from relationship_app import views # type: ignore
from django.contrib.auth.views import LoginView, LogoutView
from .views import register


urlpatterns = [
  path('books/', list_books, name='list_books'),  # Function-based view
  path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),   
  # Login view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration view
    path('register/', register, name='register'),
    
]
