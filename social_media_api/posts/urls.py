from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view({'get': 'list'}), name='feed'),  # Specify the action for the FeedView
    path('posts/&lt;int:pk&gt;/like/', PostViewSet.as_view({'post': 'like'}), name='like_post'),
    path('posts/&lt;int:pk&gt;/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='unlike_post'),
]