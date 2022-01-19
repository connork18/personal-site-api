from django.contrib.auth.models import User, Group
from .models import Post, STATUS
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # I feel like from past experience I shouldn't have to list
    # all of the different fields, but I am following the tutorial
    # from the docs
    class Meta:
        model = Post
        fields = ['title', 'slug', 'updated_on', 'created_on', 'content', 'status']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['url', 'name']