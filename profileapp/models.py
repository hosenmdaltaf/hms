from django.db import models
from django.utils.html import mark_safe
from django.conf import settings


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    # dept = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True)
    speciallist = models.CharField(max_length=200)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))