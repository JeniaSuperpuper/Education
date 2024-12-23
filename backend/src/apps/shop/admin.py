from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class Categories(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title', )}


@admin.register(Product)
class Products(admin.ModelAdmin):
    list_display = ['title','slug', 'price', 'id']
    prepopulated_fields = {'slug':('title', )}