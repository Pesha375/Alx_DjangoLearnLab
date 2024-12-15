from rest_framework import serializers
from .models import Post, Comment # type: ignore
from accounts.serializers import CustomUserSerializer # type: ignore

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