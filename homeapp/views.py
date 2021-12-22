from django.shortcuts import render
from profileapp.models import Doctor
from homeapp.models import Review,Department,Laboratory
from contactapp.models import Appointment
from django.contrib import messages
from profileapp.models import User

# dob_month = int(dob_month),
def home(request):
    doctors = Doctor.objects.all()
    # object = Doctor.objects.get(pk=pk) 
    if request.method == "POST":
        # try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phonenumber")
            date = request.POST.get("date_of_booking")
            # doctor = request.POST.get("doctor_name")
            meassage = request.POST.get("text")
            patient= request.user
            Appointment.objects.create(name=name,meassage=meassage,phone=phone,
            date=date,email=email,patient=patient)
            return render(request,'homeapp/thankyou.html')
        # except:
        #     messages.warning(request, 'Please fill up all the form feild currectly!')

    return render(request,'homeapp/index.html',{'doctors':doctors})

def about(request):
    departments = Department.objects.all()[:4]
    return render(request,'homeapp/about.html',{'departments':departments})

def doctor(request):
    doctors = Doctor.objects.all()
    return render(request,'homeapp/doctor.html',{'doctors':doctors})

def review(request):
    reviews = Review.objects.all()
    return render(request,'homeapp/review.html',{'reviews':reviews})

def test_price_list(request):
    laboratorys = Laboratory.objects.all()
    return render(request,'homeapp/test_price.html',{'laboratorys':laboratorys})


def department(request):
    departments = Department.objects.all()
    return render(request,'homeapp/services.html',{'departments':departments})

def department_details(request,pk):
    object = Department.objects.get(pk=pk)
    return render(request,'homeapp/service_details.html',{'object':object})

    
