from django.contrib.auth import views as auth_views

# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='tag_posts'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

