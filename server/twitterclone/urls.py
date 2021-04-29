from django.urls import include, path
from rest_framework import routers
from . import views
#authentication
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterAPI
from .views import LoginAPI
from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'profile',views.ProfileViewSet)
router.register(r'tweet', views.TweetViewSet)
router.register(r'UserFollowing', views.UserFollowingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addfollower/',ObtainAuthToken),
    path('tweet/',ObtainAuthToken),
    path('auth/',ObtainAuthToken.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
