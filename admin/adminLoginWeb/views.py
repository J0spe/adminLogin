from http.client import HTTPResponse
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .decorations import allowed_users
#from .forms import loginForm
#from .models import userLogin

#@admin_only
def home(request):
    return render(request, 'home.html')

@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    return render(request, 'adminPage.html')
    #template = loader.get_template('home.html')
    #return HttpResponse(template.render({}, request))

@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'studentPage.html')
