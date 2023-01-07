from rest_framework.routers import DefaultRouter
from django.urls import path, include

from project.views import (
    ProjectViewSet,
    RunProjectView,
)


router = DefaultRouter()
router.register('projects', ProjectViewSet)

app_name = 'project'


urlpatterns = [
    path('run/', RunProjectView.as_view(), name='run'),
    path('', include(router.urls)),
]
