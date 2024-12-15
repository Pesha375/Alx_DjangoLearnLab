from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer # type: ignore

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

    def mark_as_read(self, request, pk=None):
        notification = get_object_or_404(Notification, pk=pk, recipient=self.request.user) # type: ignore
        notification.read = True
        notification.save()
        return Response({'message': 'Notification marked as read.'}, status=status.HTTP_200_OK)