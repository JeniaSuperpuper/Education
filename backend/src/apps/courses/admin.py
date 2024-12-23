from django.contrib import admin
from apps.courses.models import Category, Course, Lesson


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'id']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'category', 'id']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'number', 'course']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}
