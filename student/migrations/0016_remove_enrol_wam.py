# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-23 17:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20161023_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrol',
            name='WAM',
        ),
    ]