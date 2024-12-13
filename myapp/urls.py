from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersignup/',views.usersignup),
    path('userlogout/',views.userlogout),
    path('about/',views.about),
    path('contact/',views.contact),
    path('notes/',views.notes),
    path('profile/',views.profile),
    path('uprofile/',views.uprofile),
    path('otpverify/',views.otpverify,name='otpverify')
]
