from django.urls import path

from .import views

app_name='contactapp'

urlpatterns = [ 
    path('', views.contact, name='contactpage'),
    path('appoinment/', views.appoinment, name='appoinment_page'),
]
      