# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-24 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0006_auto_20160824_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='priority',
            field=models.CharField(default='medium', max_length=6),
        ),
    ]
