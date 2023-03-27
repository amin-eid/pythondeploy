from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors):
        for key,value in errors.items():
            messages.error(request,value)
        return redirect ("/")
    else:
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        hashed=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        User.objects.create(fname=fname,lname=lname,email=email,password=hashed)
        newUser=User.objects.last().fname
        request.session['newUser']=newUser
        return redirect ("/success")
    
def login(request):
    user1=User.objects.filter(email=request.POST['email'])#[<>]
    if user1:
        logged_user=user1[0]
        if bcrypt.checkpw(request.POST['pwd'].encode(),logged_user.password.encode()):
            request.session['newUser']=logged_user.fname
            return redirect("/success")
        else:
            messages.error(request,"invalid credentials!")
            return redirect("/")
    else:
        messages.error(request,"invalid credentials!")
        return redirect("/")

def success(request):
    return render(request,"success.html")

