from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.views import generic
from blog.models import Post, Weight, Workout
from blog.serializers import PostSerializer, WeightSerializer, WorkoutSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple endpoint for retrieving blog posts
    """
    queryset = Post.objects.filter(status=1)
    lookup_field = 'slug'
    serializer_class = PostSerializer

class WorkoutViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple endpoint for retrieving workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class WeightViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple endpoint for retrieving workouts
    """
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

