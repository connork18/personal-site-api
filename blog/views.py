from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple endpoint for retrieving blog posts
    """
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer
