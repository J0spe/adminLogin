# Generated by Django 4.1.1 on 2022-10-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentAccount', '0002_remove_studentaccount_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaccount',
            name='major',
            field=models.CharField(choices=[('General Engineering', 'General Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Computer Engineering', 'Computer Engineering')], max_length=50, null=True),
        ),
    ]