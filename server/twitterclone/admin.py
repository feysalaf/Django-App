from django.contrib import admin
from .models import User,Tweet,UserFollowing,Profile
# Register your models here.
#admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(UserFollowing)
admin.site.register(Profile)
