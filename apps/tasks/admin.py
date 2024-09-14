from django.contrib import admin
from apps.tasks.models import *
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created')
    search_fields = ("title", 'description')
