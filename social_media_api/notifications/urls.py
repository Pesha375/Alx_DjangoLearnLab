from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notifications/&lt;int:pk&gt;/mark_as_read/', NotificationViewSet.as_view({'post': 'mark_as_read'}), name='mark_notification_as_read'),
]