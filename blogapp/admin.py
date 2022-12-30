from django.contrib import admin
from .models import Blog,Comment
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title','writer','post_date','image_tag')
    summernote_fields = ('content',)

admin.site.register(Blog,BlogAdmin)

admin.site.register(Comment)
