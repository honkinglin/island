# Generated by Django 5.1.4 on 2025-01-10 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='City Name')),
                ('desc', models.CharField(max_length=200, verbose_name='City Description')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Add Time')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Organization Name')),
                ('desc', models.TextField(verbose_name='Organization Description')),
                ('tag', models.CharField(default='National', max_length=10, verbose_name='Organization Tag')),
                ('category', models.CharField(default='School', max_length=20, verbose_name='Organization Category')),
                ('click_nums', models.IntegerField(default=0, verbose_name='Click Number')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Favorite Number')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='Organization Image')),
                ('address', models.CharField(max_length=150, verbose_name='Organization Address')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('students', models.IntegerField(default=0, verbose_name='Number of Students')),
                ('course_nums', models.IntegerField(default=0, verbose_name='Number of Courses')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Add Time')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Teacher Name')),
                ('work_years', models.IntegerField(default=0, verbose_name='Working Years')),
                ('work_company', models.CharField(max_length=50, verbose_name='Company')),
                ('work_position', models.CharField(max_length=50, verbose_name='Position')),
                ('points', models.CharField(max_length=50, verbose_name='Teaching Characteristics')),
                ('click_nums', models.IntegerField(default=0, verbose_name='Click Number')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Favorite Number')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Add Time')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgnization.courseorg', verbose_name='Organization')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teacher',
            },
        ),
    ]
