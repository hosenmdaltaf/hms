from django.contrib import admin

from homeapp.models import Department,Laboratory,Review,Gallery,Services,Diagnostic,Hospital
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Review)
admin.site.register(Gallery)

class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('testname','costoftest','resulttime')
admin.site.register(Laboratory,LaboratoryAdmin)

class DiagnosticAdmin(SummernoteModelAdmin):
    list_display = ('name','image_tag')
    summernote_fields = ('details',)
admin.site.register(Diagnostic,DiagnosticAdmin)

class HospitalAdmin(SummernoteModelAdmin):
    list_display = ('name','image_tag')
    summernote_fields = ('details',)
admin.site.register(Hospital,HospitalAdmin)

class ServicesAdmin(SummernoteModelAdmin):
    list_display = ('name','image_tag')
    summernote_fields = ('details',)
admin.site.register(Services,ServicesAdmin)

class DepartmentAdmin(SummernoteModelAdmin):
    list_display = ('name','image_tag')
    summernote_fields = ('details',)
admin.site.register(Department,DepartmentAdmin)

