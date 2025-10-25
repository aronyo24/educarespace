from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'image_tag', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')
    ordering = ('teacher_id',)

    def image_tag(self, obj):
       
        try:
            if obj.photo and hasattr(obj.photo, 'url'):
                url = obj.photo.url
            else:
                media_url = getattr(settings, 'MEDIA_URL', '/media/')
                if not media_url.endswith('/'):
                    media_url = media_url + '/'
                url = media_url + 'default.jpg'

            if not url.startswith('/'):
                url = '/' + url

            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:4px;" />', url)
        except Exception:
            return ''

    image_tag.short_description = 'Photo'


admin.site.register(Teacher, TeacherAdmin)
