from django.shortcuts import render ,redirect
from home.models import Contact
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout , login
from django.contrib.auth.models import User , auth


# Create your views here.
def home(request):
   return render(request, 'index.html')

def aboutus(request):
   return render(request, 'aboutus.html')

def contactus(request):
    if request.method =="POST":
        n = request.POST.get('name')
        e= request.POST.get('email')
        p = request.POST.get('phone')
        d= request.POST.get('desc')
        contactdata = Contact(name= n,email= e,phone=p,desc= d,date=datetime.today())
        contactdata.save()
    return render(request, "contactus.html")

def gardeningtools(request):
   return render(request, 'gardeningtools.html')

def plants(request):
   return render(request, 'plants.html')

def seeds(request):
   return render(request, 'seeds.html')

def userlogin(request):
   

    if request.method=="POST":
        username= request.POST.get('username') 
        password  = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invaild username or password , please try again")
            return render(request,'userlogin.html')
    return render(request,'userlogin.html')


def register(request):
     if request.method=="POST":
        username= request.POST.get('username') 
        password  = request.POST.get('password')
        confirmpassword  = request.POST.get('confirmpassword')
        email =request.POST.get('email')
        
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username,password=password,email= email)
                user.save()
                return redirect('/userlogin')
        else:
            messages.info(request,"Passwords do not match ,try again")
            return render(request,'register.html')
       
     return render(request,'register.html')
 

def userlogout(request):
     if request.user.is_anonymous:
        return render(request,'userlogin.html')
        
     return render(request,"userlogout.html")

def logingout(request):
    logout(request)
    return redirect('/userlogin')
    
    

