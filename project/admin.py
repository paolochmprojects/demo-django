from django.contrib import admin
from .models import Project
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

admin.site.register(Project)
admin.site.register(CustomUser, UserAdmin)
