from rest_framework import serializers
from .models import Notification
from accounts.serializers import CustomUserSerializer

class NotificationSerializer(serializers.ModelSerializer):
    recipient = CustomUserSerializer(read_only=True)
    actor = CustomUserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'created_at', 'read']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'created_at', 'read']