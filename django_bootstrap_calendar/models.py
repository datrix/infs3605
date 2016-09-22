# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils import datetime_to_timestamp
from student.models import student
from apptType.models import apptType
from django.contrib.auth.models import User


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('', _('Normal')),
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'),  primary_key = True)
    url = models.CharField(max_length=9, verbose_name=_('URL'), null=True, blank=True)
    css_class = models.CharField(blank=True, max_length=20, verbose_name=_('Priority'),
                                 choices=CSS_CLASS_CHOICES)
    start = models.DateTimeField(verbose_name=_('Start Time & Date'))
    end = models.DateTimeField(verbose_name=_('End Time & Date'), null=True,
                               blank=True)
    zID = models.ForeignKey(student, on_delete = models.CASCADE, null=True)
    notes = models.CharField(max_length = 400, null=True, blank=True)
    ugc = models.CharField(max_length = 100, null=True)
    apptType = models.ForeignKey(apptType, on_delete = models.CASCADE, null=True)

    @property
    def start_timestamp(self):
        """
        Return start date as timestamp
        """
        return datetime_to_timestamp(self.start)

    @property
    def end_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.end)

    def __unicode__(self):
        return self.title
      
class consultType(models.Model):
  title = models.ForeignKey(CalendarEvent, on_delete = models.CASCADE, null = True)
  apptType = models.ForeignKey(apptType)