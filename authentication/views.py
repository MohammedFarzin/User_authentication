from email import message
from django.views.decorators.cache import never_cache
from http.client import HTTPResponse
from turtle import clear
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from authentication.models import Technologies

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        tech = Technologies.objects.all()
        return render(request, "authentication/index.html", {'tech' : tech})
    else:
        return redirect('signin')


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password1']

            user = authenticate(username = username, password = password1)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.error(request, 'Bad credentials')
                return redirect('home')
    return render(request, 'authentication/signin.html')

# @never_cache
# def signup(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         if password1 == password2:
#             if User.objects.filter(username = username).exists():
#                 messages.info(request, 'Username taken')
#                 return redirect('signup')
#             elif User.objects.filter(email = email).exists():
#                 messages.info(request, 'Email taken')
#                 return redirect('signup')
#             else:
#                 myuser = User.objects.create_user(username, email, password1)
#                 myuser.first_name = fname
#                 myuser.last_name = lname
#                 myuser.save()
#         else:
#             messages.info(request, 'Password not match')
#             return redirect('signup')

#         return redirect('/')
#     else:
#         return render(request, 'authentication/signup.html')


                

    #     messages.success(request, 'Your account has been successfully created')
    #     return redirect('signin')

        
    

    # return render(request, 'authentication/signup.html')


def signout(request):
    if request.user.is_authenticated:
        
        logout(request) 
        messages.success(request, "Logout successfully")
    return redirect('signin')


