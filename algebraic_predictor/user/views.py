from rest_framework import generics, permissions, authentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from user import serializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class AuthTokenView(ObtainAuthToken):
    serializer_class = serializers.TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
