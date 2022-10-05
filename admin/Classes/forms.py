from django import forms


DEGREE_CHOICES = [('Electrical Engineering', 
    'Computer Engineering', 'General Engineering')]

class studentForm(forms.Form):
    degree = forms.CharField(label="Choose your degree", widget=forms.Select(choices=DEGREE_CHOICES))
