from django import forms
from django.views.generic import View
from .models import CalendarEvent
from .models import apptType
from datetimewidget.widgets import DateTimeWidget
  
class EventForm(forms.ModelForm):
  class Meta: #information about the class
    model = CalendarEvent
    fields =['title', 'css_class', 'start', 'end', 'zID', 'notes', 'ugc']
    dateTimeOptions = {
    'daysOfWeekDisabled':[0,6],
    'format':'dd/mm/yyyy HH:ii P',
    'hoursDisabled':[0,9],
    }
    
    widgets = {
      'start': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, options=dateTimeOptions), 
      'end': DateTimeWidget(attrs={'id':"endtime"}, usel10n=True, bootstrap_version=3, options=dateTimeOptions)
    }

  #class Meta:
  #  model = apptType
   # fields = ['apptType']

