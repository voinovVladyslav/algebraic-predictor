from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.TextField(max_length=255, blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    algebraic_model = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "%s's project #%s" % (self.user, self.id)
