from django.contrib import admin
from .models import Category, Course


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'id']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'category', 'id']
    prepopulated_fields = {'slug': ('title',)}
