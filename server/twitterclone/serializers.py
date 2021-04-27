from rest_framework import serializers

from .models import User,Tweet,Following

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'age',
                  'user_name')

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
