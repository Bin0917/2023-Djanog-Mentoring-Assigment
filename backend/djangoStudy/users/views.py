from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import views as auth_views

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        email =  request.POST.get('email')
        password =  request.POST.get('password')
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        
        context={
            'user':user
        }
        return render(request, 'login.html', context)

def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')
        
        user = authenticate(request, username=user_id, password=user_pw)
        
        if user is not None:
            login(request, user=user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
        
def logout_view(request):
    logout(request)
    return render(request, 'login.html')