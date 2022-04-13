from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'login.html')

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loggingIn(request):
    if request.method=="POST":    
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        if(username1 == "" or password1 == ""):
            messages.info(request, 'Please fill all fields')
            return redirect("/userAccounts/loggingIn/")
        user = authenticate(username=username1, password=password1)
        if user is not None:
            login(request, user)
            return redirect("/books/")

            # A backend authenticated the credentials
        else:
            messages.info(request, 'Inavlid Username/Password')
            return redirect("/userAccounts/loggingIn/")
    return render(request, 'login.html')

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutView(request):
    pass


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerScreenView(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'register.html')


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerView(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(username == "" or password == "" or email == "" or firstname == ""):
            messages.info(request, 'Please fill all fields')
            return redirect("/userAccounts/registerScreen/")

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect("/userAccounts/registerScreen/")

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect("/userAccounts/registerScreen/")
        user = User.objects.create_user(
            username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        if user is not None:
            login(request, user)

            msg=f"Hello! {firstname} 👋,\nWelcome to the Innovator's Library 📚. You have successfully registered to our Library(username : {username}) 🔥🔥. Our platform is very new, so help us by checking the functionalities of our platform. Do check out our collection, and you can tell us which other books you need ✨✨.\nDon't forget to submit the feedback form, and all your suggestions are appreciated(until and unless they are reasonable 🙂).\n\nTill then, Happy Reading🥳🤗,\nThe Innovator's Team"
        
            send_mail("Registration Successful", msg,settings.EMAIL_HOST_USER,[email],fail_silently=False)
            
            send_mail(f"{firstname} Registered",f"{firstname} with email id:{email} and username:{username} registered to our library.",settings.EMAIL_HOST_USER,['innovators.library@gmail.com'],fail_silently=False)

            return redirect("/books/")
