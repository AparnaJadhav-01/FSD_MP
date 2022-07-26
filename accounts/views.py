from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/accounts/login')

    else:
        return render(request,'apts/login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('/accounts/register')
        else:
            user = User.objects.create_user(username=username,password=password1,email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('/accounts/login')
        
    else:
        return render(request,'apts/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')