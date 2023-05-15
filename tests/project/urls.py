from django.urls import reverse


PROJECTS_URL = reverse('project:project-list')

def get_project_detail_url(pk):
    return reverse('project:project-detail', kwargs={'pk': pk})
