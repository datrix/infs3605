
# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils import datetime_to_timestamp
from student.models import student
from apptType.models import apptType
from django.contrib.auth.models import User
import django_filters
from datetimewidget.widgets import DateTimeWidget
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget

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
    start = models.DateTimeField(verbose_name=_('Start Date & Time'))
    end = models.DateTimeField(verbose_name=_('End Date & Time'), null=True,
                               blank=True)
    zID = models.ForeignKey(student, related_name='studentzID', on_delete = models.CASCADE, null=True)
    notes = models.CharField(max_length = 400, null=True, blank=True, verbose_name=_('Notes'))
    ugc = models.CharField(max_length = 100, null=True, verbose_name=('Staff'))
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
  
class ConsultationFilter(django_filters.FilterSet):
    CSS_CLASS_CHOICES = (
      ('', _('')),
      ('event-success', _('Low')),
      ('event-warning', _('Medium')),
      ('event-important', _('High')),
    )
    title = django_filters.CharFilter(name='title', lookup_expr = 'icontains')
    priority = django_filters.ChoiceFilter(name = 'css_class',choices=CSS_CLASS_CHOICES)
    start = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'DD/MM/YYYY'}))
    zID = django_filters.ModelChoiceFilter(queryset=student.objects.all())

    class Meta:
      model = CalendarEvent
      fields = ['title']
      
      dateTimeOptions = {
       'daysOfWeekDisabled':[0,6],
       'format':'dd/mm/yyyy HH:ii P',
       'hoursDisabled':[0,9],
       }
      
      widgets = {
            #Use localization and bootstrap 3
            'start': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, options=dateTimeOptions),
        }
  
  