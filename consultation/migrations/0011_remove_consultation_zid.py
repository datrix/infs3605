# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-26 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0010_auto_20160919_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='zID',
        ),
    ]