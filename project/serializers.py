from rest_framework import serializers
from .models import Project
from task.serializers import TaskSerializer

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
     
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created', 'tasks']
