import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from project.models import Project

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def save(self, *args, **kwargs):
        print(self.password)
        return super().save()

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks', null=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
