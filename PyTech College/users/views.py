from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib import messages


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'login.html')

def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check credentials
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In!")

            return redirect("/")

        else:
            messages.success(request, "Check Login Credetials")

            return render(request,'login.html')

    return render(request,'login.html')

def userlogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")

    return redirect("/")


def uregister(request):
    if request.method=='POST':
        #fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
        #number=request.POST.get('number')
        #city=request.POST.get('city')
        #pcode=request.POST.get('pcode')

        user=User.objects.create_user(username,email,password)
        user.save()
        messages.success(request, "Account Created Successfully!!!")
        return redirect("/login")


    return render(request,'uregister.html')

# Create your views here.
