"""adminLoginWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.urls import path
#from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views
from Classes import views as cl_views
from studentAccount import views as st_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('adminPage', views.adminPage, name="adminPage"),
    #path('accounts/login', views.new, name="login"),
    path('insertClasses', cl_views.insertClasses, name="insertClasses"),
    path('updateClasses', cl_views.updateClasses, name="updateClasses"),
    #path('successAddClass', auth_views.TemplateView.as_view(template_name="successAddClass.html"), name='successAddClass'),
    path('studentPage', views.studentPage, name="studentPage"),
    path('updateStudent', st_views.updateStudent, name="updateStudent"),

    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name="logout"),
]

urlpatterns += staticfiles_urlpatterns()
