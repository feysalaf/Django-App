from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Tweet,Profile,UserFollowing
from django.contrib.auth.models import User, Group


from django.contrib.auth import get_user_model

Users = get_user_model()
# User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email','password')
class UserSerializer(serializers.ModelSerializer):

    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()


    class Meta:
        model = Users
        fields = (
            "id",
            "email",
            "username",
            "following",
            "followers",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data




class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id',
                  'user_name',
                  'age')
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
class UserFollowingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ('id',
                  'user_id',
                  'following_user_id')

class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ("id", "following_user_id", "created")

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created")
