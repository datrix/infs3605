# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-23 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_remove_enrol_wam'),
    ]

    operations = [
        migrations.CreateModel(
            name='coopPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='placementCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='Company')),
            ],
        ),
    ]
