"""
URL configuration for eknowint project.

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
#from re import template
from telnetlib import AUTHENTICATION
from django.contrib import admin
from django.urls import path, include

from .views import Main
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",Main.as_view(), name="Main"),
    path("ipaddr/",include("ipaddr.urls")),
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("ek_contact/",include("ek_contact.urls")),
    path("site_contact/", include("site_contact.urls")),
]
