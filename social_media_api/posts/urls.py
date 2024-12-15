# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view({'get': 'list'}), name='feed'),
    path('posts/<int:pk>/like/', LikeViewSet.as_view({'post': 'like'}), name='like_post'),
    path('posts/<int:pk>/unlike/', LikeViewSet.as_view({'post': 'unlike'}), name='unlike_post'),
]