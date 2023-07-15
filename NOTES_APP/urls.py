"""
URL configuration for NOTES_APP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Notes_Organizer.urls')),
    path('sign_up',include('Notes_Organizer.urls')),
    path('login',include('Notes_Organizer.urls')),
    path('signuphandle',include('Notes_Organizer.urls')),
    path('loginhandle',include('Notes_Organizer.urls')),
    path('home',include('Notes_Organizer.urls')),
    path('savenotes',include('Notes_Organizer.urls')),
    path('delete',include('Notes_Organizer.urls')),
    path('theme',include('Notes_Organizer.urls')),
    path('logout',include('Notes_Organizer.urls')),
    # path('profile',include('Notes_Organizer.urls')),
]
