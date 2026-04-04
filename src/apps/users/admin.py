from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.users.models import BaseGroup, BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(UserAdmin):
    """Админка пользователей"""

    list_display = ("__str__", "email", "is_active", "is_staff", "date_joined")


admin.site.unregister(Group)


@admin.register(BaseGroup)
class BaseGroupAdmin(admin.ModelAdmin):
    """Админка групп"""
