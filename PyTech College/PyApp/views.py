from django.shortcuts import render
from PyApp.models import Contact
from datetime import datetime
from django.contrib import messages




def  index(request):
    return render(request,'index.html')


def  about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        description=request.POST.get('description')
        contact=Contact(fullname=fullname, email=email, phone=phone, subject=subject, description=description,date=datetime.today())
        contact.save()
        messages.success(request, "Query Submitted Successfully!")

    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')
# Create your views here.
