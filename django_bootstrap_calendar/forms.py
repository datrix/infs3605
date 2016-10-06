from django import forms
from django.views.generic import View
from .models import CalendarEvent
from .models import apptType
from datetimewidget.widgets import DateTimeWidget
#from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class EventForm(forms.ModelForm): 
    
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Fieldset(
        'title',
        'css_class',
        'start',
        'end',
        'zID',
        'notes',
        'apptType'
      ),
      ButtonHolder(
        Submit('submit', 'Submit', css_class='button white')
      )
    )
    
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
    
class EditEventForm(forms.ModelForm):
    class Meta: 
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
    