from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name='home'),
    path("login/",views.userlogin,name='login'),
    path("logout/",views.userlogout,name='logout'),
    path("uregister/",views.uregister,name='uregister'),    


]