from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets

from .serializers import UserSerializer, TweetSerializer, FollowingSerializer
from .models import User,Tweet,Following


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('id')
    serializer_class = TweetSerializer

class FollowingViewSet(viewsets.ModelViewSet):
    queryset = Following.objects.all().order_by('id')
    serializer_class = FollowingSerializer
