# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-08 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_student_startyear'),
        ('django_bootstrap_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='zID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
