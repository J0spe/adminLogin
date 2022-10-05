from django.db import models
from django.contrib.auth.models import User

class studentAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PID = models.CharField(max_length=20)
    #username = User.username
    major = models.CharField(max_length=50,
        choices=[('General Engineering', 'General Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Computer Engineering', 'Computer Engineering')], null=True)

    def __str__(self):
        return self.user.username