# param/admin.py
from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_line', 'phone_number', 'website', 'address', 'logo_display')
    search_fields = ('name', 'target_line', 'phone_number', 'website', 'address')
    list_filter = ('name', 'target_line')
    readonly_fields = ('logo_display',)

    def logo_display(self, obj):
        if obj.logo:
            return '<img src="{}" width="50" height="50" />'.format(obj.logo.url)
        return ''
    logo_display.allow_tags = True
    logo_display.short_description = 'Logo'

admin.site.register(School, SchoolAdmin)
