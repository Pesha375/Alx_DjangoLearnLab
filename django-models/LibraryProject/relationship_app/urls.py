from django.urls import path
from .views import list_books, LibraryDetailView
from relationship_app import views # type: ignore



urlpatterns = [
  path('books/', list_books, name='list_books'),  # Function-based view
  path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),   
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('register/', views.register_view, name='register'),
    
    
]
