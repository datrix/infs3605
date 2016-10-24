from django import forms
from django.forms import inlineformset_factory
from django.views.generic import View
from django_bootstrap_calendar.models import CalendarEvent
from datetimewidget.widgets import DateTimeWidget
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Reset, Button, Row
from crispy_forms.bootstrap import InlineField, FormActions, InlineRadios

class consultForm(forms.ModelForm):
                               
  def __init__(self, *args, **kwargs):
    super(consultForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Fieldset(
        'Filter by:',
        'title',
        'Priority',
        Div(
          Div('start', css_class='col-md-5',),
          css_class='row',
        ),
        'zID',
      ),
      
      FormActions(
        Submit('submit', 'Submit'),
        Button('cancel', 'Cancel', css_class='btn-default', onclick="window.history.back()")
      )
    )
    
  class Meta: #information about the class
    model = CalendarEvent
    exclude = ['url']
    
    
    dateTimeOptions = {
       'daysOfWeekDisabled':[0,6],
       'format':'dd/mm/yyyy HH:ii P',
       'hoursDisabled':[0,9],
       }
    
    widgets = {
          'start': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, options=dateTimeOptions),
    }  