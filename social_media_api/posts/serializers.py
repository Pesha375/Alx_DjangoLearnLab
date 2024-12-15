from rest_framework import serializers
from .models import Post, Comment, Like
from accounts.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def create(self, validated_data):
        author = self.context['request'].user
        post = Post.objects.create(author=author, **validated_data)
        return post

class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def create(self, validated_data):
        author = self.context['request'].user
        post_id = validated_data.pop('post_id')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, author=author, **validated_data)
        return comment

class LikeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = validated_data.pop('post_id')
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            raise serializers.ValidationError('You have already liked this post.')
        return like