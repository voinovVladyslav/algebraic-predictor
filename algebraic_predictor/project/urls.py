from rest_framework.routers import DefaultRouter

from project.views import ProjectViewSet


router = DefaultRouter()
router.register('projects', ProjectViewSet)

app_name = 'project'


urlpatterns = router.urls
