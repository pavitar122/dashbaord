from django.shortcuts import render, redirect
from django.contrib import messages
from login_system.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        profile_picture = request.FILES['image']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address_line1 = request.POST['address_line1']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        value = request.POST["dropdown"]
        print(value)

        if password != confirm_password:
            messages.warning(request, "Password and Confirm Password do not match.")
            return redirect("/signup")
    
        if Doctor.objects.filter(email=email).first() or Patient.objects.filter(email=email).first() :
            messages.warning(request,"Email already exists")
            return redirect("/signup")
        
        if Doctor.objects.filter(username=username).first() or Doctor.objects.filter(username=username).first():
            messages.warning(request,"Username already exists")
            return redirect("/signup")
        
        if value == "value1":
            doctor = Doctor(first_name=first_name,
                            last_name=last_name,
                            profile_picture=profile_picture,
                            username = username,
                            email=email,
                            password=password,
                            address_line1 = address_line1,
                            city= city,
                            state = state,
                            pincode=pincode
                            )
            
            doctor.save()
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active =True
            user.save()

            return redirect("/login")
        elif value == "value2":
             
            patient = Patient(first_name=first_name,
                            last_name=last_name,
                            profile_picture=profile_picture,
                            username = username,
                            email=email,
                            password=password,
                            address_line1 = address_line1,
                            city= city,
                            state = state,
                            pincode=pincode
                            )
            
            patient.save()
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active =True
            user.save()
            return redirect("/login")

    return render(request, "signup.html")

def login_view(request):
    if request.method=="POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
                login(request, user)
                doctor_data = Doctor.objects.filter(username=username).first()
                patient_data = Patient.objects.filter(username=username).first()

                if doctor_data:
                    return render(request, "dashboard.html", {"heading": "Doctor", "data": doctor_data})
                else:
                    return render(request, "dashboard.html", {"heading": "Patient", "data": patient_data})
         else:
              messages.warning(request, "Username or Password is wrong.")
              return redirect("/login")
                
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/")