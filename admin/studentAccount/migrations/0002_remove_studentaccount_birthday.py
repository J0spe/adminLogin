# Generated by Django 4.1.1 on 2022-10-01 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentAccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentaccount',
            name='birthday',
        ),
    ]
