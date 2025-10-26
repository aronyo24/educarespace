from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'fname', 'lname', 'image_tag', 'email')
    search_fields = ('fname', 'lname', 'email')

    def image_tag(self, obj):
        """Return an HTML <img> tag for the admin list display.

        Uses the student photo if available, otherwise falls back to
        MEDIA_URL + 'default.jpg'.
        """
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


admin.site.register(Student, StudentAdmin)