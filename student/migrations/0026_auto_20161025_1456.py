# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-25 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_auto_20161025_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrol',
            name='grade',
            field=models.IntegerField(null=True, verbose_name='Mark'),
        ),
    ]
