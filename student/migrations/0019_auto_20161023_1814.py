# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-23 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20161023_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='coopplacement',
            name='firstPref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FirstPreference', to='student.placementCompanies'),
        ),
        migrations.AddField(
            model_name='coopplacement',
            name='secondPref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SecondPreference', to='student.placementCompanies'),
        ),
        migrations.AddField(
            model_name='coopplacement',
            name='thirdPref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ThirdPreference', to='student.placementCompanies'),
        ),
    ]
