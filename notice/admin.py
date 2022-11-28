from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Notice, NoticeAdmin)
