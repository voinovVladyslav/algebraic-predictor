from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet
from project.serializers import ProjectSerializer
from project.models import Project


class ProjectViewSet(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
