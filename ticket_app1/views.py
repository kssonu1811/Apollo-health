from django.shortcuts import render
from ticket_app1.models import Appointment
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        phone1 = request.POST['phone1']
        c_add = request.POST['c_add']
        c_city = request.POST['c_city']
        c_state = request.POST['c_state']
        c_zip = request.POST['c_zip']
        p_add = request.POST['p_add']
        p_city = request.POST['p_city']
        p_state = request.POST['p_state']
        email = request.POST['email']
        p_zip = request.POST['p_zip']
        a_date_time = request.POST['a_date_time']
        messagees = request.POST['messagees']
    

        appointment = Appointment(first_name=first_name,last_name=last_name,phone=phone,phone1=phone1,c_add=c_add,c_city=c_city,c_state=c_state,c_zip=c_zip,p_add=p_add,p_city=p_city,p_state=p_state,email=email,p_zip=p_zip,a_date_time=a_date_time,messagees=messagees)
        appointment.save()
        messages.success(request,'Thankyou, Your request has been submitted . We will get back to you shortly')
    return render(request, 'phase1/home.html')
