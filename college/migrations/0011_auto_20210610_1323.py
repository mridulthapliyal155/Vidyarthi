# Generated by Django 3.0.4 on 2021-06-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_auto_20210610_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_info',
            name='city',
            field=models.CharField(choices=[('Kanpur', 'Kanpur'), ('Lucknow', 'Lucknow'), ('Varanasi', 'Varanasi'), ('Allahbad', 'Allahbad'), ('Greater Noida', 'Greater Noida'), ('Noida', 'Noida'), ('Ghaziabad', 'Ghaziabad'), ('Sultanpur', 'Sultanpur'), ('Gorakhpur', 'Gorakhpur'), ('Agra', 'Agra'), ('Jhansi', 'Jhansi'), ('Sadabad Jakhaiva', 'Sadabad Jakhaiva'), ('Raebareli', 'Raebareli'), ('Bareilly', 'Bareilly'), ('Muradanagar', 'Muradanagar'), ('Jaunpur', 'Jaunpur'), ('Amethi', 'Amethi'), ('Mathura', 'Mathura'), ('New Delhi', 'New Delhi')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='college_info',
            name='state',
            field=models.CharField(choices=[('Uttar Pradesh', 'Uttar Pradesh'), ('Delhi', 'Delhi')], default=None, max_length=100, null=True),
        ),
    ]
