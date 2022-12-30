from django.db import models
from homeapp.models import Department
from profileapp.models import Doctor 
from datetime import datetime


class Appointment(models.Model):  
    name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    department_name = models.CharField(null=True,blank=True,max_length=400)
    doctor_name = models.CharField(null=True,blank=True,max_length=400)
    date = models.DateTimeField(default=datetime.now, blank=True)
    meassage =models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    meassage =models.TextField()

    def __str__(self):
        return str(self.name)
