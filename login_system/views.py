from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from login_system.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import os
from django.http import JsonResponse
from django.core import serializers

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

        file_name, file_extension = os.path.splitext(profile_picture.name)
        new_file_name = f"{username}{file_extension}"
        profile_picture.name = new_file_name

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
                request.session['user'] = username
                return redirect("/dashboard")       
         else:
              messages.warning(request, "Username or Password is wrong.")
              return redirect("/login")
                
    return render(request, "login.html")


def dashbaord(request):
    data = request.session.get('user')
    doctor_data = Doctor.objects.filter(username=data).first()
    patient_data = Patient.objects.filter(username=data).first()
    if doctor_data:
        request.session['heading'] = "Doctor"
        return render(request, "dashboard.html", {"heading": "Doctor", "data": doctor_data})
    else:
        request.session['heading'] = "Patient"
        return render(request, "dashboard.html", {"heading": "Patient", "data": patient_data})


def add_blog(request):
    data = request.session.get('user')
    heading = request.session.get('heading')
    doctor_data = Doctor.objects.filter(username=data).first()
    if request.method=="POST":
        title = request.POST['title']
        image = request.FILES['image']
        category = request.POST['category']
        summary = request.POST['summary']
        content = request.POST['content']
        is_draft = request.POST.get('draft') == 'on'


        
        blog_data = BlogPost.objects.filter(username = data, title=title).first()
        if blog_data:
            blog_data.title = title
            blog_data.image = image
            blog_data.category = category
            blog_data.summary = summary
            blog_data.content = content
            blog_data.is_draft = False
            blog_data.save()

            return redirect(f"/{heading}_blogs")

       
    
        
        else:
            
            if BlogPost.objects.filter(title=title).first():
                messages.warning(request,"Use another title.")
                return redirect("/add_blog")
            blog = BlogPost(
                title=title,
                image=image,
                category=category,
                summary= summary,
                content= content,
                username= doctor_data.username,
                name = doctor_data.first_name + " " + doctor_data.last_name,
                is_draft= is_draft,

            )
            blog.save()
            return redirect(f"/{heading}_blogs")

    return render(request, "add_blog.html")

def doctor_blogs(request):
    return render(request, "Doctor_blogs.html")

def patient_blogs(request):
    return render(request, "Patient_blogs.html")

def blog(request, post_title):
    data = request.session.get('user')
    title = post_title
    view_blog = BlogPost.objects.filter(username = data, title=title).first()
 
    return render(request, "blog.html", {"data": view_blog})



def logout_view(request):
    if  request.session['user']:
        del request.session['user']
        del request.session['heading']
        logout(request)
        return redirect("/")
    else:
        logout(request)
        return redirect("/")

def delete_draft(request, post_title):
    data = request.session.get('user')
    title = post_title
    blog_data = BlogPost.objects.filter(username = data, title=title).first()
    blog_data.delete()
    messages.warning(request,"Draft had been Deleated")
    return redirect("/add_blog")


def api_blog_posts(request):
    blog_posts = BlogPost.objects.filter(is_draft=False)
    serialized_data = serializers.serialize('json', blog_posts)
    return JsonResponse({'data': serialized_data}, safe=False)


def api_draft_blog(request):
    username = request.user.username
    blog_posts = BlogPost.objects.filter(username= username,  is_draft=True)
    serialized_data = serializers.serialize('json', blog_posts)
    return JsonResponse({'data': serialized_data}, safe=False)
   
   