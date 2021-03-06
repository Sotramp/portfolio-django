from django.contrib import admin
from django.utils.text import Truncator
from .models import Project, UploadImg

# Project class
class ProjectAdmin(admin.ModelAdmin):
    # List configuration
    # list_filter and ordering are of type list, that's why there's a "useless" space.
    list_display   = ('name', 'date', 'overview')
    # Automatic slug filling
    prepopulated_fields = {'slug': ('name', ), }
    list_filter    = ('name', )
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('name', 'desc')

    def overview(self, project):
        # If the description exceeds 30 characters, cut
        return Truncator(project.desc).chars(30, truncate='..')

    overview.short_description = 'Project description'

    # Form configuration
    fieldsets = (
       ('Informations', {
            'fields': ('name', 'slug', 'image', 'labels')
        }),
        ('Les liens', {
            'description': 'Non-compulsory filling.',
            'fields': ('github', 'demo')
        }),
        ('Description du projet', {
           'description': 'This field accepts HTML tags.',
           'fields': ('desc', )
        }),
    )

# Upload image class
class UploadImgAdmin(admin.ModelAdmin):
    # List configuration
    list_display   = ('projet', 'name')
    ordering       = ('projet', )
    search_fields  = ('name', )

# Model insertion
admin.site.register(Project, ProjectAdmin)
admin.site.register(UploadImg, UploadImgAdmin)