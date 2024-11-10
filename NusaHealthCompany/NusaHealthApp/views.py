from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .decorators import admin_required
from .models import Logo, ImageSlider, HeroSection, ServiceSection
import os

def Home(request):
    logo_instance = Logo.objects.first()
    image_slider = ImageSlider.objects.first()
    hero = HeroSection.objects.first()
    services = ServiceSection.objects.first()

    context = {
        'section': 'home',
        'logo': logo_instance,
        'slider': image_slider,
        'hero': hero,
        'services': services
    }
    return render(request, 'Home/index.html', context)

def About(request):
    logo_instance = Logo.objects.first()

    context = {
        'section': 'about',
        'logo': logo_instance
    }
    return render(request, 'Home/about.html', context)

def Contact(request):
    logo_instance = Logo.objects.first()

    context = {
        'section': 'contact',
        'logo': logo_instance
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

    logo_instance = Logo.objects.first()

    context = {
        'section': 'sign-in',
        'logo': logo_instance
    }
    return render(request, 'Home/sign-in.html', context)

def SignOut(request):
    logout(request)
    return redirect('sign-in') 

@admin_required()
def Dashboard(request):
    logo_instance = Logo.objects.first()

    context = {
        'section': 'dashboard',
        'logo': logo_instance
    }
    return render(request, 'Dashboard/index.html', context)

@admin_required()
def BlogsManagement(request):
    logo_instance = Logo.objects.first()

    context = {
        'section': 'blogs-management',
        'logo': logo_instance
    }
    return render(request, 'Dashboard/blogs-management.html', context)

@admin_required()
def ActivitiesManagement(request):
    logo_instance = Logo.objects.first()

    context = {
        'section': 'activities-management',
        'logo': logo_instance
    }
    return render(request, 'Dashboard/activities-management.html', context)

@admin_required()
def ContentManagement(request):
    logo_instance = Logo.objects.first()
    image_slider = ImageSlider.objects.first()
    hero = HeroSection.objects.first()
    services = ServiceSection.objects.first()

    context = {
        'section': 'content-management',
        'logo': logo_instance,
        'slider': image_slider,
        'hero': hero,
        'services': services,
    }
    return render(request, 'Dashboard/content-management.html', context)

def delete_old_file(file_path):
    if file_path and os.path.exists(file_path):
        os.remove(file_path)

@admin_required()
def UploadLogo(request):
    if request.method == 'POST':
        logo_instance = Logo.objects.first() or Logo()

        if 'primaryLogo' in request.FILES:
            if logo_instance.primary_logo:
                delete_old_file(logo_instance.primary_logo.path)
            logo_instance.primary_logo = request.FILES['primaryLogo']

        if 'secondaryLogo' in request.FILES:
            if logo_instance.secondary_logo:
                delete_old_file(logo_instance.secondary_logo.path)
            logo_instance.secondary_logo = request.FILES['secondaryLogo']

        logo_instance.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Logos updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadSlider(request):
    if request.method == 'POST':
        slider_instance = ImageSlider.objects.first() or ImageSlider()

        if 'slider1' in request.FILES:
            if slider_instance.image1:
                delete_old_file(slider_instance.image1.path)
            slider_instance.image1 = request.FILES['slider1']

        if 'slider2' in request.FILES:
            if slider_instance.image2:
                delete_old_file(slider_instance.image2.path)
            slider_instance.image2 = request.FILES['slider2']

        if 'slider3' in request.FILES:
            if slider_instance.image3:
                delete_old_file(slider_instance.image3.path)
            slider_instance.image3 = request.FILES['slider3']

        if 'slider4' in request.FILES:
            if slider_instance.image4:
                delete_old_file(slider_instance.image4.path)
            slider_instance.image4 = request.FILES['slider4']

        if 'slider5' in request.FILES:
            if slider_instance.image5:
                delete_old_file(slider_instance.image5.path)
            slider_instance.image5 = request.FILES['slider5']

        slider_instance.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Images slider updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadHero(request):
    if request.method == 'POST':
        hero_instance = HeroSection.objects.first() or HeroSection()

        hero_text = request.POST.get('hero_text', '').strip()
        hero_instance.hero_text = hero_text if hero_text else ""

        if 'hero_image' in request.FILES:
            if hero_instance.hero_image:
                delete_old_file(hero_instance.hero_image.path)
            hero_instance.hero_image = request.FILES['hero_image']

        hero_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Hero section updated successfully.',
            'hero_image_name': os.path.basename(hero_instance.hero_image.name) if hero_instance.hero_image else None,
            'hero_text': hero_instance.hero_text
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

