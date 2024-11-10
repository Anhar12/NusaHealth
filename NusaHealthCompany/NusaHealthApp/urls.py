from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    path('sign-in', views.SignIn, name='sign-in'),
    path('sign-out', views.SignOut, name='sign-out'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('dashboard/content-management', views.ContentManagement, name='content-management'),
    path('dashboard/blogs-management', views.BlogsManagement, name='blogs-management'),
    path('dashboard/activities-management', views.ActivitiesManagement, name='activities-management'),
]
