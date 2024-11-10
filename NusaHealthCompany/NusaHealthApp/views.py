from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .decorators import admin_required

def Home(request):
    context = {
        'section' : 'home'
    }
    return render(request, 'Home/index.html', context)

def About(request):
    context = {
        'section' : 'about'
    }
    return render(request, 'Home/about.html', context)

def Contact(request):
    context = {
        'section' : 'contact'
    }
    return render(request, 'Home/contact.html', context)

def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if not username or not password:
            return JsonResponse({'is_superuser': False, 'error': 'Username and password are required.'}, status=400)

        if user is not None and user.is_superuser and user.is_staff:
            login(request, user)
            return JsonResponse({'is_superuser': True})
        else:
            return JsonResponse({'is_superuser': False, 'error': 'Invalid username or password.'}, status=403)

    context = {
        'section': 'sign-in'
    }
    return render(request, 'Home/sign-in.html', context)

def SignOut(request):
    logout(request)
    return redirect('home') 

@admin_required()
def Dashboard(request):
    context = {
        'section': 'dashboard'
    }
    return render(request, 'Dashboard/index.html', context)

@admin_required()
def ContentManagement(request):
    context = {
        'section': 'content-management'
    }
    return render(request, 'Dashboard/content-management.html', context)

@admin_required()
def BlogsManagement(request):
    context = {
        'section': 'blogs-management'
    }
    return render(request, 'Dashboard/blogs-management.html', context)

@admin_required()
def ActivitiesManagement(request):
    context = {
        'section': 'activities-management'
    }
    return render(request, 'Dashboard/activities-management.html', context)