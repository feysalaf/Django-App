from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer, TweetSerializer, RegisterSerializer, ProfileSerializer,UserFollowingSerializer
from .models import User,Tweet,Profile,UserFollowing
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, schema



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('id')
    serializer_class = TweetSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)


class UserFollowingViewSet(viewsets.ModelViewSet):
    queryset = UserFollowing.objects.all().order_by('id')
    serializer_class = UserFollowingSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        print(request.user.username)
        return super(LoginAPI, self).post(request, format=None)

class AddFollower(  APIView):
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):

        UserFollowing.objects.create(user=self.request.data.get('userID'),following_user=self.request.data.get('followID'))
        return render_to_response({'status':status.HTTP_200_OK, 'data':"", 'message':"follow"+str(follow.user_id)})
