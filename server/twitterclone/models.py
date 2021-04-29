from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    fields = ["username", "password"]

class Profile(models.Model):
    user_name  = models.CharField(max_length=200)
    age = models.TextField()
    def __str__(self):
        return self.user_name


class Tweet(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    tweet = models.TextField()
#
# class Following(models.Model):
#     user = models.ForeignKey(Profile,on_delete=models.CASCADE)
#     following = models.CharField(max_length=50)

class UserFollowing(models.Model):
    user = models.ForeignKey(Profile, related_name="followings",on_delete=models.CASCADE)
    following_user = models.ForeignKey(Profile, related_name="followers",on_delete=models.CASCADE)
    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)
 
