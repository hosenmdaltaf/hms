from django.contrib import admin
from profileapp.models import Doctor
from django_summernote.admin import SummernoteModelAdmin

class DoctorAdmin(SummernoteModelAdmin):
    list_display = ('name','image_tag','speciallist')
    summernote_fields = ('details',)
admin.site.register(Doctor,DoctorAdmin)  