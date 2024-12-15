from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/&lt;int:pk&gt;/like/', LikeViewSet.as_view({'post': 'like'}), name='like_post'),
    path('posts/&lt;int:pk&gt;/unlike/', LikeViewSet.as_view({'post': 'unlike'}), name='unlike_post'),
    path('feed/', FeedView.as_view(), name='feed'), # type: ignore
]