from tokenize import group
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.REST_AUTH_CALLBACK_URL


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        # users = User.objects.all().order_by('-date_joined')
        # serializer = UserSerializer(users, many=True)
        # return Response(serializer.data)
        data = [
            {'name': 'John', 'age': 30},
            {'name': 'Alex', 'age': 29},
            {'name': 'Lucas', 'age': 33},
            {'name': 'Emily', 'age': 40},
            {'name': 'Atom', 'age': 66},
        ]
        return Response(data)

class GroupView(APIView):
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # group = Group.objects.all()
        # serializer = GroupSerializer(group, many=True)
        # return Response(serializer.data)
        return Response([])

