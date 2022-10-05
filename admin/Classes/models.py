#from tkinter import Widget
#from math import degrees
#from unittest.util import _MAX_LENGTH
#from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import AbstractUser
 

class Classes(models.Model):
    Course = models.CharField(max_length=8)
    Major = models.CharField(max_length=20, null=True)
    Credit_Hours = models.IntegerField(null=True)
    Semester_Taught = models.CharField(max_length = 6, null=True)
    Required_Passing_Grade = models.CharField(max_length=2, null=True)


#DEGREE_CHOICES = [('Electrical Engineering', 
    #'Computer Engineering', 'General Engineering')]

#class studentForm(forms.Form):
    #degree = forms.CharField(label="Choose your degree", widget=forms.Select(choices=DEGREE_CHOICES))
