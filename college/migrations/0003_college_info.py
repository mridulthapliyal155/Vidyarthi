# Generated by Django 3.0.4 on 2020-11-30 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_line_chart'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=100)),
                ('college_email', models.CharField(max_length=100)),
                ('max_placements', models.CharField(max_length=100)),
                ('college_fees', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.College')),
            ],
        ),
    ]
