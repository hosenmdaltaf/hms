from django.db import models
from profileapp.models import Doctor
from django.utils.html import mark_safe
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details=models.TextField()
    deptdoctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True,related_name='doctor_name')

    def __str__(self):
        return str(self.name) 

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))

class Services(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))

class Diagnostic(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))

class Hospital(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))
    

class Laboratory(models.Model):
    testname=models.CharField(max_length=100)
    costoftest=models.IntegerField(blank=True, null=True)
    resulttime=models.TimeField()

    def __str__(self):
        return str(self.testname)

    
class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery_img', blank=True, null=True)
    title=models.CharField( max_length=20, blank=True, null=True)
    text=models.CharField(max_length=50, blank=True, null=True)


class Review(models.Model):
    name=models.CharField( max_length=20, blank=True, null=True)
    title=models.CharField( max_length=20, blank=True, null=True)
    text=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.name)
