from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Tweet,Following

from django.contrib.auth.models import User, Group

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username',
#                   'password')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id',
                  'user',
                  'tweet')
class FollowingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Following
        fields = ('id',
                  'user',
                  'following')
