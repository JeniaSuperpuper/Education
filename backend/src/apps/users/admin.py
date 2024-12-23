from django.contrib import admin
from apps.users.models import CustomUser, Child, Teacher


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'id']

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'parent', 'id']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']