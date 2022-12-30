from django.shortcuts import render
from profileapp.models import Doctor
from homeapp.models import Review,Department,Laboratory,Services,Hospital,Diagnostic
from contactapp.models import Appointment
from django.contrib import messages

# dob_month = int(dob_month),
def home(request):
    doctors = Doctor.objects.all()[:4]
    departments = Department.objects.all()[:6]
    reviews = Review.objects.all()
    services = Services.objects.all()[:4]
    # object = Doctor.objects.get(pk=pk) 
    if request.method == "POST":
        # try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            department = request.POST.get("department")
            Appointment.objects.create(name=name,phone=phone,
            date=date, department_name=department)
            return render(request,'global/thankyou.html')
        # except:
        #     messages.warning(request, 'Please fill up all the form feild currectly!')

    return render(request,'homeapp/index.html',{'doctors':doctors,
    'departments':departments,'reviews':reviews,'services':services})

def about(request):
    doctors = Doctor.objects.all()[:4]
    reviews = Review.objects.all()
    return render(request,'homeapp/about.html',{'reviews':reviews,'doctors':doctors,})

def doctor(request):
    doctors = Doctor.objects.all()
    return render(request,'homeapp/doctor.html',{'doctors':doctors})

def doctor_details(request,pk):
    if request.method == "POST":
    # try:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        doctor_name = request.POST.get("doctor_name")
        Appointment.objects.create(name=name,phone=phone,
        date=date, doctor_name=doctor_name)
        return render(request,'global/thankyou.html')
    object = Doctor.objects.get(pk=pk)
    return render(request,'homeapp/doctor_details.html',{'object':object})

def review(request):
    reviews = Review.objects.all()
    return render(request,'homeapp/review.html',{'reviews':reviews})

def test_price_list(request):
    laboratorys = Laboratory.objects.all()
    return render(request,'homeapp/test_price.html',{'laboratorys':laboratorys}) 


def services(request): 
    services = Services.objects.all() 
    return render(request,'homeapp/services.html',{'services':services})

def services_details(request,pk):
    if request.method == "POST":
        # try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            service_name = request.POST.get("service_name")
            Appointment.objects.create(name=name,phone=phone,
            date=date, department_name=service_name)
            return render(request,'global/thankyou.html') 
    object = Services.objects.get(pk=pk) 
    return render(request,'homeapp/services_details.html',{'object':object})

def department_details(request,pk):
    if request.method == "POST":
        # try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            department = request.POST.get("department")
            Appointment.objects.create(name=name,phone=phone,
            date=date, department_name=department)
            return render(request,'global/thankyou.html')
    object = Department.objects.get(pk=pk)
    return render(request,'homeapp/depertment_details.html',{'object':object}) 

def diagnostic_details(request,pk):  
    if request.method == "POST":
        # try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            department = request.POST.get("department")
            Appointment.objects.create(name=name,phone=phone,
            date=date, department_name=department) 
            return render(request,'global/thankyou.html')
    object = Diagnostic.objects.get(pk=pk)
    return render(request,'homeapp/diagnostic_details.html',{'object':object}) 

def hospital(request): 
    hospital = Hospital.objects.all() 
    return render(request,'homeapp/hospital.html',{'hospital':hospital})  

def hospital_details(request,pk):
    if request.method == "POST":
        # try:
            name = request.POST.get("name") 
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            department = request.POST.get("department")
            Appointment.objects.create(name=name,phone=phone,
            date=date, department_name=department) 
            return render(request,'global/thankyou.html')
    object = Hospital.objects.get(pk=pk)
    return render(request,'homeapp/hospital_details.html',{'object':object}) 




    
