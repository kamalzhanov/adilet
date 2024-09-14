from django.contrib import admin
from apps.post.models import *
# Register your models here.

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')
    search_fields = ("title", 'description')
