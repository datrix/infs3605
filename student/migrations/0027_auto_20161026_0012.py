# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-26 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_auto_20161025_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrol',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Course'),
        ),
    ]
