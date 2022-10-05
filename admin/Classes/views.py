from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect

from .models import Classes
from adminLoginWeb import decorations

@decorations.allowed_users(allowed_roles=['admin'])
def insertClasses(request):
    if request.method == 'POST':
        course = request.POST['Course']
        major = request.POST['Major']
        CH = request.POST['Credit_Hours']
        ST = request.POST['Semester_Taught']
        RPG = request.POST['Required_Passing_Grade']

        if not (Classes.objects.filter(Course=course).exists()):
            my = Classes(Course=course,Major=major,Credit_Hours=CH,Semester_Taught=ST,Required_Passing_Grade=RPG)
            my.save()
            return render(request, "successAddClass.html")
        return render(request, 'failAddClass.html')

    else:
        return render(request, "insertClasses.html")

@decorations.allowed_users(allowed_roles=['admin'])
def updateClasses(request):
    if request.method == 'POST':
        course = request.POST['Course']
        major = request.POST['Major']
        CH = request.POST['Credit_Hours']
        ST = request.POST['Semester_Taught']
        RPG = request.POST['Required_Passing_Grade']

        if (Classes.objects.filter(Course=course).exists()):
            event = Classes.objects.get(Course=course)
            event.delete()
            my = Classes(Course=course,Major=major,Credit_Hours=CH,Semester_Taught=ST,Required_Passing_Grade=RPG)
            my.save()
            return render(request, "successUpdateClass.html")
        return render(request, 'failUpdateClass.html')

    else:
        return render(request, "updateClasses.html")





    