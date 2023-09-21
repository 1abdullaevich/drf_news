from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['created_at']
