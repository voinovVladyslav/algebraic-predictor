from rest_framework import serializers
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'source', 'algebraic_model']
        read_only_fields = ['id']
