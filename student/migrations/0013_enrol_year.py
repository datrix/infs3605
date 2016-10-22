# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-22 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_enrol_sem_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrol',
            name='year',
            field=models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2016, max_length=4, verbose_name='year'),
        ),
    ]
