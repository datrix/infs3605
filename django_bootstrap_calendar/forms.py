from django import forms
from django.views.generic import View
from .models import CalendarEvent
from .models import apptType
from datetimewidget.widgets import DateTimeWidget
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin import widgets


class EventForm(forms.ModelForm):
   
  class Meta: #information about the class
    model = CalendarEvent
    exclude = ['ugc', 'url']
     
    
    dateTimeOptions = {
       'daysOfWeekDisabled':[0,6],
       'format':'dd/mm/yyyy HH:ii P',
       'hoursDisabled':[0,9],
       }
    
    CHOICES=[(' ','Normal'),
         ('event-warning','Warning')]
    
    widgets = {
          'start': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, options=dateTimeOptions), 
          'end': DateTimeWidget(attrs={'id':"endtime"}, usel10n=True, bootstrap_version=3, options=dateTimeOptions)
    }
