from django.shortcuts import render
from contactapp.models import Contact,Appointment
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            meassage  = request.POST.get("message")
            phone = request.POST.get("phonenumber") 
            Contact.objects.create(name=name,meassage=meassage,phone=phone)
            return render(request,'global/thankyou.html') 
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    return render(request,'contactapp/contact.html')


def appoinment(request): 
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            date = request.POST.get("date")
            meassage  = request.POST.get("message")
            phone = request.POST.get("phone") 
            Appointment.objects.create(name=name,meassage=meassage,phone=phone,date=date)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    return render(request,'contactapp/appoinment.html')



