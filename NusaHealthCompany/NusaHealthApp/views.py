from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .decorators import admin_required
from .models import Logo, ImageSlider, HeroSection, ServiceSection, PhilosphySection, VisionMissionSection, BusinessStructure, SolutionsSection, ContactSection, LocationSection
from markdown2 import markdown
import os

def Home(request):
    logo_instance = Logo.objects.first()
    image_slider = ImageSlider.objects.first()
    hero = HeroSection.objects.first()
    services = ServiceSection.objects.first()
    contact = ContactSection.objects.first()

    context = {
        'section': 'home',
        'logo': logo_instance,
        'slider': image_slider,
        'hero': hero,
        'services': services,
        'contact': contact
    }
    return render(request, 'Home/index.html', context)

def About(request):
    logo_instance = Logo.objects.first()
    philosophy = PhilosphySection.objects.first()
    vision_mission = VisionMissionSection.objects.first()
    business_structure = BusinessStructure.objects.first()
    solutions = SolutionsSection.objects.first()
    contact = ContactSection.objects.first()

    if vision_mission and vision_mission.vision_text:
        vision = vision_mission.vision_text
    else:
        vision = ""
    
    if vision_mission and vision_mission.mission_text:
        mission_text_html = markdown(vision_mission.mission_text)
    else:
        mission_text_html = ""

    context = {
        'section': 'about',
        'logo': logo_instance,
        'philosophy': philosophy,
        'vision': vision,
        'mission': mission_text_html,
        'business_structure': business_structure,
        'solutions': solutions,
        'contact': contact
    }
    return render(request, 'Home/about.html', context)

def Blogs(request):
    logo_instance = Logo.objects.first()
    
    context = {
        'section': 'blogs',
        'logo': logo_instance
    }
    return render(request, 'Home/blogs.html', context)

def Activities(request):
    logo_instance = Logo.objects.first()
    
    context = {
        'section': 'activities',
        'logo': logo_instance
    }
    return render(request, 'Home/activities.html', context)
    
def Contact(request):
    logo_instance = Logo.objects.first()
    contact = ContactSection.objects.first()
    location = LocationSection.objects.first()

    context = {
        'section': 'contact',
        'logo': logo_instance,
        'contact': contact,
        'location': location
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
    philosophy = PhilosphySection.objects.first()
    vision_mission = VisionMissionSection.objects.first()
    business_structure = BusinessStructure.objects.first()
    solutions = SolutionsSection.objects.first()
    contact = ContactSection.objects.first()
    location = LocationSection.objects.first()

    context = {
        'section': 'content-management',
        'logo': logo_instance,
        'slider': image_slider,
        'hero': hero,
        'services': services,
        'philosophy': philosophy,
        'vision_mission': vision_mission,
        'business_structure': business_structure,
        'solutions': solutions,
        'contact': contact,
        'location': location
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
            'message': 'Hero section updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadServices(request):
    if request.method == 'POST':
        services_instance = ServiceSection.objects.first() or ServiceSection()

        service_title1 = request.POST.get('service_title1')
        services_instance.service_title1 = service_title1 if service_title1 else ""
        service_description1 = request.POST.get('service_description1', '').strip()
        services_instance.service_description1 = service_description1 if service_description1 else ""

        service_title2 = request.POST.get('service_title2')
        services_instance.service_title2 = service_title2 if service_title2 else ""
        service_description2 = request.POST.get('service_description2', '').strip()
        services_instance.service_description2 = service_description2 if service_description2 else ""

        service_title3 = request.POST.get('service_title3')
        services_instance.service_title3 = service_title3 if service_title3 else ""
        service_description3 = request.POST.get('service_description3', '').strip()
        services_instance.service_description3 = service_description3 if service_description3 else ""

        if 'service_image1' in request.FILES:
            if services_instance.service_image1:
                delete_old_file(services_instance.service_image1.path)
            services_instance.service_image1 = request.FILES['service_image1']

        if 'service_image2' in request.FILES:
            if services_instance.service_image2:
                delete_old_file(services_instance.service_image2.path)
            services_instance.service_image2 = request.FILES['service_image2']

        if 'service_image3' in request.FILES:
            if services_instance.service_image3:
                delete_old_file(services_instance.service_image3.path)
            services_instance.service_image3 = request.FILES['service_image3']

        services_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Services section updated successfully.'
        })

@admin_required()
def UploadPhilosophy(request):
    if request.method == 'POST':
        philosophy_instance = PhilosphySection.objects.first() or PhilosphySection()

        philosophy_text = request.POST.get('philosophy_text', '').strip()
        philosophy_instance.philosophy_text = philosophy_text if philosophy_text else ""

        if 'philosophy_image' in request.FILES:
            if philosophy_instance.philosophy_image:
                delete_old_file(philosophy_instance.philosophy_image.path)
            philosophy_instance.philosophy_image = request.FILES['philosophy_image']

        philosophy_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Philosophy section updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadVisionMission(request):
    if request.method == 'POST':
        vision_mission_instance = VisionMissionSection.objects.first() or VisionMissionSection()

        vision_text = request.POST.get('vision_text', '').strip()
        vision_mission_instance.vision_text = vision_text if vision_text else ""

        mission_text = request.POST.get('mission_text', '').strip()
        vision_mission_instance.mission_text = mission_text if mission_text else ""
        
        vision_mission_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Vision and Mission section updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadBusinessStructure(request):
    if request.method == 'POST':
        business_instance = BusinessStructure.objects.first() or BusinessStructure()
        
        name_ceo = request.POST.get('name_ceo')
        business_instance.name_ceo = name_ceo if name_ceo else ""
        
        name_coo = request.POST.get('name_coo')
        business_instance.name_coo = name_coo if name_coo else ""
        
        name_cto = request.POST.get('name_cto')
        business_instance.name_cto = name_cto if name_cto else ""
        
        name_cfo = request.POST.get('name_cfo')
        business_instance.name_cfo = name_cfo if name_cfo else ""
        
        name_cmo = request.POST.get('name_cmo')
        business_instance.name_cmo = name_cmo if name_cmo else ""

        if 'business1' in request.FILES:
            if business_instance.image_ceo:
                delete_old_file(business_instance.image_ceo.path)
            business_instance.image_ceo = request.FILES['business1']

        if 'business2' in request.FILES:
            if business_instance.image_coo:
                delete_old_file(business_instance.image_coo.path)
            business_instance.image_coo = request.FILES['business2']

        if 'business3' in request.FILES:
            if business_instance.image_cfo:
                delete_old_file(business_instance.image_cfo.path)
            business_instance.image_cfo = request.FILES['business3']

        if 'business4' in request.FILES:
            if business_instance.image_cto:
                delete_old_file(business_instance.image_cto.path)
            business_instance.image_cto = request.FILES['business4']

        if 'business5' in request.FILES:
            if business_instance.image_cmo:
                delete_old_file(business_instance.image_cmo.path)
            business_instance.image_cmo = request.FILES['business5']

        business_instance.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Business structure updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadSolutions(request):
    if request.method == 'POST':
        solutions_instance = SolutionsSection.objects.first() or SolutionsSection()

        solution_title1 = request.POST.get('solution_title1')
        solutions_instance.solution_title1 = solution_title1 if solution_title1 else ""
        solution_description1 = request.POST.get('solution_description1', '').strip()
        solutions_instance.solution_description1 = solution_description1 if solution_description1 else ""

        solution_title2 = request.POST.get('solution_title2')
        solutions_instance.solution_title2 = solution_title2 if solution_title2 else ""
        solution_description2 = request.POST.get('solution_description2', '').strip()
        solutions_instance.solution_description2 = solution_description2 if solution_description2 else ""

        solution_title3 = request.POST.get('solution_title3')
        solutions_instance.solution_title3 = solution_title3 if solution_title3 else ""
        solution_description3 = request.POST.get('solution_description3', '').strip()
        solutions_instance.solution_description3 = solution_description3 if solution_description3 else ""

        solutions_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Solutions section updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadContact(request):
    if request.method == 'POST':
        contact_instance = ContactSection.objects.first() or ContactSection()

        phone_number = request.POST.get('phone_number')
        contact_instance.phone_number = phone_number if phone_number else ""

        whatsapp = request.POST.get('whatsapp')
        contact_instance.whatsapp = whatsapp if whatsapp else ""

        email = request.POST.get('email')
        contact_instance.email = email if email else ""

        instagram = request.POST.get('instagram')
        contact_instance.instagram = instagram if instagram else ""

        facebook = request.POST.get('facebook')
        contact_instance.facebook = facebook if facebook else ""
        
        address = request.POST.get('address', '').strip()
        contact_instance.address = address if address else ""

        contact_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Contact section updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@admin_required()
def UploadLocation(request):
    if request.method == 'POST':
        location_instance = LocationSection.objects.first() or LocationSection()

        try:
            latitude = float(request.POST.get('latitude'))
            longitude = float(request.POST.get('longitude'))
        except (TypeError, ValueError):
            return JsonResponse({
                'status': 'error',
                'message': 'Latitude and longitude must be valid floating-point numbers.'
            }, status=400)

        location_instance.latitude = latitude
        location_instance.longitude = longitude
        location_instance.save()

        location_instance.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Location section updated successfully.'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)