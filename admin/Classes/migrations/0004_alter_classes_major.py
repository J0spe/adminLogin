# Generated by Django 4.1.1 on 2022-10-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0003_classes_credit_hours_classes_major_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='Major',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
