# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-24 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_auto_20161023_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coopplacement',
            name='firstPref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FirstPreference', to='student.placementCompanies', verbose_name='First Preference'),
        ),
    ]
