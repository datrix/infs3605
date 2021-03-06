# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-21 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_student_startyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(max_length=100, verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, verbose_name='E-mail Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='f_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='l_name',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='startYear',
            field=models.IntegerField(verbose_name='Year Started'),
        ),
    ]
