from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from project.serializers import ProjectSerializer
from project.models import Project

from console.tasks import send_email


class ProjectViewSet(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RunProjectView(GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        token = Token.objects.get(user=request.user)
        send_email.delay(token.key)
        return Response({'ok': 1})
