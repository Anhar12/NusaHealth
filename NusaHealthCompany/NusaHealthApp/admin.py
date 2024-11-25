from django.contrib import admin
from .models import Blogs, Activities

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'status', 'publish')
    list_filter = ('status', 'created', 'publish', 'author', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'publish')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
