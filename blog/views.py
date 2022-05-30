from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.views import generic
from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple endpoint for retrieving blog posts
    """
    queryset = Post.objects.filter(status=1)
    lookup_field = 'slug'
    serializer_class = PostSerializer

# class PostDetailViewSet(generic.detailview):
#   """
#   An endpoint to retrieve a specific blog based on URL
#   """
#   model = Post