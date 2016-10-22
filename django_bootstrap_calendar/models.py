
# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils import datetime_to_timestamp
from student.models import student
from apptType.models import apptType
from django.contrib.auth.models import User
import django_filters


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        #(None), 
        ('event-success', _('Low')),
        ('event-warning', _('Medium')),
        ('event-important', _('High')),
    )
    
    
    title = models.CharField(max_length=255, verbose_name=_('Title'),  primary_key = True)
    url = models.CharField(max_length=9, verbose_name=_('URL'), null=True, blank=True)
    css_class = models.CharField(blank=False, max_length=20, verbose_name=_('Priority'),
                                 choices=CSS_CLASS_CHOICES, null = True, default = 'event-success')
    start = models.DateTimeField(verbose_name=_('Start Time & Date'))
    end = models.DateTimeField(verbose_name=_('End Time & Date'), null=True,
                               blank=True)
    zID = models.ForeignKey(student, on_delete = models.CASCADE, null=True)
    notes = models.CharField(max_length = 400, null=True, blank=True, verbose_name=_('Notes'))
    ugc = models.CharField(max_length = 100, null=True, verbose_name=_('Staff'))
    apptType = models.ForeignKey(apptType, on_delete = models.CASCADE, null=True, verbose_name=_('Appointment Type'))

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
  
  
  