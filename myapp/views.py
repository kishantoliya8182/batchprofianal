from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from BatchProject import settings

# Create your views here.

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def userlogin(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)

        uid=userSignup.objects.get(username=unm)
        print("UserID:",uid.id)
        if user:
            print("Login successfully!")
            msg="Login successfully!"
            request.session['user']=unm
            request.session['uid']=uid.id
            return redirect('/')
        else:
           return redirect('/')
    return render(request,'userlogin.html',{'msg':msg})


def usersignup(request):
    msg=""
    if request.method=='POST':
        newReq=signupform(request.POST)
        username=""
        if newReq.is_valid():
            username=newReq.cleaned_data.get('username')
            try:
                userSignup.objects.get(username=username)
                print("Username is already exists!")
                msg="Username is already exists!"
            except userSignup.DoesNotExist:
                newReq.save()
                print("Signup Successfully!")

                #Email Sending Code
                global otp
                otp=random.randint(11111,99999)
                sub="Your One Time Password"
                msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 97247 99469 | sanket@tops-int.com"
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                
                #send_mail(subject="Your One Time Password",message=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 97247 99469 | sanket@tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=['kishantoliya4@gmail.com','meetladva1684@gmail.com','kevalkotadiya509@gmail.com','pratixagoswami2000@gmail.com','k.p.jogi89@gmail.com','radhikapithadia123@gmail.com'])
                return redirect('otpverify')
        
        else:
            print(newReq.errors)
    return render(request,'usersignup.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        newCont=contactForm(request.POST)
        if newCont.is_valid():
            newCont.save()
            print("Your response has been submitted!")

            #Email Sending
            sub="Thankyou!"
            msg=f"Hello User!\n\nThanks for connecting with us!\nWe will contact you shortly!\n\nThanks & Regards\n+919724799469 | sanket.tops@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
        else:
            print(newCont.errors)
    return render(request,'contact.html',{'user':user})

def notes(request):
    msg=""
    user=request.session.get('user')
    data=mynotes.objects.all()
    if request.method=='POST':
        newNotes=notesForm(request.POST,request.FILES)
        if newNotes.is_valid():
            newNotes.save()
            return render(request,'notes.html',{'user':user,'msg':msg,'data':data})
        else:
            print(newNotes.errors)
            msg="Error!Somthing went wrong...Try again!"
    return render(request,'notes.html',{'user':user,'msg':msg,'data':data})

def profile(request):
    msg=""
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateReq=updateform(request.POST,instance=cuser)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('/')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!"
    return render(request,'profile.html',{'user':user,'cuser':cuser,'msg':msg})

def otpverify(request):
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("Verification done!")
            return redirect('userlogin')
        else:
            print("Error!Invalid OTP")
            msg="Error!Invalid OTP"
    return render(request,'otpverify.html',{'msg':msg})

def uprofile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    data=userSignup.objects.get(id=uid)
    return render(request,'uprofile.html',{'data':data})

