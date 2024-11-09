from django.shortcuts import render

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