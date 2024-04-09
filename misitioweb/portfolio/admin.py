from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display =('title', 'description', 'url')
    ordering = ('description','url')
    search_fields = ('title','description','url',
        'created')
    date_hierarchy = 'updated'
    list_filter = ('title','url')

admin.site.register(Project, ProjectAdmin)