from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('blogs', views.Blogs, name='blogs'),
    path('activities', views.Activities, name='activities'),
    path('contact', views.Contact, name='contact'),
    path('sign-in', views.SignIn, name='sign-in'),
    path('sign-out', views.SignOut, name='sign-out'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('dashboard/content-management', views.ContentManagement, name='content-management'),
    path('dashboard/blogs-management', views.BlogsManagement, name='blogs-management'),
    path('dashboard/activities-management', views.ActivitiesManagement, name='activities-management'),
    path('dashboard/upload-logo', views.UploadLogo, name='upload-logo'),
    path('dashboard/upload-slider', views.UploadSlider, name='upload-slider'),
    path('dashboard/upload-hero', views.UploadHero, name='upload-hero'),
    path('dashboard/upload-services', views.UploadServices, name='upload-services'),
    path('dashboard/upload-philosophy', views.UploadPhilosophy, name='upload-philosophy'),
    path('dashboard/upload-vision-mission', views.UploadVisionMission, name='upload-vision-mission'),
    path('dashboard/upload-business-structure', views.UploadBusinessStructure, name='upload-business-structure'),
    path('dashboard/upload-solutions', views.UploadSolutions, name='upload-solutions'),
    path('dashboard/upload-contact', views.UploadContact, name='upload-contact'),
    path('dashboard/upload-location', views.UploadLocation, name='upload-location'),
]
