# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-24 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20161024_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrol',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_old', to='course.course', unique=True),
        ),
    ]
