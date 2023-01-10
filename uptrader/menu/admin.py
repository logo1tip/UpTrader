from django.contrib import admin

from .models import Head, Child


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    list_display_links = ('head',  'name')
    

admin.site.register(Child, ChildAdmin)
admin.site.register(Head)
