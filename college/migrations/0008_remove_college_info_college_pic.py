# Generated by Django 3.0.4 on 2021-01-20 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_college_college_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college_info',
            name='college_pic',
        ),
    ]
