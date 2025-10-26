from django.contrib import admin

# Register your models here.
from .models import Blooklist

class BlooklistAdmin(admin.ModelAdmin):
    list_display = ('blooklist_id', 'title', 'author', 'cover_image')
    search_fields = ('title', 'author')
    ordering = ('blooklist_id',)

admin.site.register(Blooklist, BlooklistAdmin)