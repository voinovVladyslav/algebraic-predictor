from rest_framework.routers import DefaultRouter
from django.urls import path, include

from project.views import (
    ProjectViewSet,
    run_project,
)


router = DefaultRouter()
router.register('projects', ProjectViewSet)

app_name = 'project'


urlpatterns = [
    path('projects/<int:pk>/run/', run_project, name='project-run'),
    path('', include(router.urls)),
]
