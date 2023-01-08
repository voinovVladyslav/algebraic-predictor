from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from project.serializers import ProjectSerializer
from project.models import Project

from console.tasks import send_log


class ProjectViewSet(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def run(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        project = self.get_object()
        send_log.delay(project.source, token.key)
        return Response({'status': 'run'})


run_project = ProjectViewSet.as_view({
    'get': 'run'
})
