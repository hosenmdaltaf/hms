from django.urls import path

from .import views

app_name='homeapp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('doctor/', views.doctor, name='doctorpage'),
    path('doctor/<int:pk>', views.doctor_details, name='doctor_details_page'),
    path('reviews/', views.review, name='reviewpage'),
    path('services/', views.services, name='services_page'),
    path('services_details/<int:pk>', views.services_details, name='services_details_page'),
    path('department/<int:pk>', views.department_details, name='departmentdetails'),
    path('test_price_list/', views.test_price_list, name='test_price_list'), 
    path('diagnostic/<int:pk>', views.diagnostic_details, name='diagnostic_details'),
    path('hospital/', views.hospital, name='hospital_page'),
    path('hospital/<int:pk>', views.hospital_details, name='hospital_details'),
] 