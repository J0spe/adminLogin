#from os import major
from django.shortcuts import render
from .models import studentAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your views here.
def updateStudent(request):
    if request.method == 'POST':
        degree = request.POST['major']
        #form = UserCreationForm(request.POST)
        #if form.is_valid():
            #user = form.save()
        
        my = studentAccount(user=User.username,PID='test',major=degree)
        my.save()

        return render(request, "successUpdateClass.html")
        #return render(request, 'failUpdateClass.html')

    else:
        return render(request, "updateStudent.html")