# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-26 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20160926_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='degreeCode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.degree'),
        ),
    ]
