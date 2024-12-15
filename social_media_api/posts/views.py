# posts/views.py
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing blog posts.
    Supports listing, creating, retrieving, updating, and deleting posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        """
        Automatically set the author of the post to the currently logged-in user.
        """
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """
        Allow filtering of posts by title and content via query parameters.
        """
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        content = self.request.query_params.get('content', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if content:
            queryset = queryset.filter(content__icontains=content)

        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments on posts.
    Supports listing, creating, retrieving, updating, and deleting comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        """
        Automatically set the author of the comment to the currently logged-in user.
        """
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """
        Allow filtering of comments by post_id via query parameters.
        """
        queryset = super().get_queryset()
        post_id = self.request.query_params.get('post_id', None)

        if post_id:
            try:
                queryset = queryset.filter(post__id=int(post_id))
            except ValueError:
                # Handle invalid post_id gracefully
                queryset = queryset.none()

        return queryset

class FeedView(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin):
    """
    View for generating a feed of posts from users that the current user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Return posts from users that the current user follows, ordered by creation date.
        """
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')