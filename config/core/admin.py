# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'tags')

admin.site.register(Tag)
admin.site.register(ContactMessage)