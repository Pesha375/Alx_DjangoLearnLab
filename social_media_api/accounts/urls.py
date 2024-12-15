from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/&lt;int:user_id&gt;/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/&lt;int:user_id&gt;/', UnfollowUserView.as_view(), name='unfollow_user'),
]