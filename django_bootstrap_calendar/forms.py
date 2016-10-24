from django import forms
from django.forms import inlineformset_factory
from django.views.generic import View
from .models import CalendarEvent
from .models import apptType
from student.models import student
from student.forms import StudentForm
from datetimewidget.widgets import DateTimeWidget
#from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Reset, Button, Row
from crispy_forms.bootstrap import InlineField, FormActions, InlineRadios
from django.contrib.auth.models import User



class EventForm(forms.ModelForm):

  ugc = forms.ModelChoiceField(queryset=User.objects.all())
                               
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.fields['ugc'].label = "Staff"
    self.fields['zID'].label = "Student"
    self.fields['title'].label = "Consultation Name"
    self.helper.layout = Layout(
        'title',
        Div(
          Div('zID', css_class='col-md-5',),
          Div(css_class = 'col-md-1'),
          InlineRadios('css_class', css_class = 'col-md-4',),
          css_class='row',
        ),
        Div(
          Div('start', css_class='col-md-5',),
          Div(css_class = 'col-md-1'),
          Div('end', css_class='col-md-5',),
          css_class='row',
        ),
        'apptType',
        'notes',
        Div('ugc')
      ,
      
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
    
    CHOICES=[(' ','Normal'),
         ('event-warning','Warning')]
    
    widgets = {
          'start': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, options=dateTimeOptions), 
          'end': DateTimeWidget(attrs={'id':"endtime"}, usel10n=True, bootstrap_version=3, options=dateTimeOptions),
          'notes': forms.Textarea(attrs={'rows': 5})
    }  
    
class addNotes(forms.ModelForm):
  #ugc = forms.ModelChoiceField(queryset=User.objects.all())
                               
  def __init__(self, *args, **kwargs):
    super(addNotes, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        #'Please add notes:',
        Div('notes'
           ),
      FormActions(
        Submit('submit', 'Submit'),
        Button('cancel', 'Cancel', css_class='btn-default', onclick="window.history.back()")
      )
    )
    
 
    
  class Meta: #information about the class
    model = CalendarEvent
    exclude = ['title', 'url','css_class', 'start', 'end', 'zID','apptType','ugc']    
    widgets = {
          #'start': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3, options=dateTimeOptions), 
          #'end': DateTimeWidget(attrs={'id':"endtime"}, usel10n=True, bootstrap_version=3, options=dateTimeOptions),
          'notes': forms.Textarea(attrs={'rows': 10})
    }  

  #title = forms.CharField(disabled=True)
  #zID = forms.CharField(disabled=True)
  #css_class = forms.CharField(disabled=True)
  #start = forms.DateTimeField(disabled=True)
  #end = forms.DateTimeField(disabled=True)
  #ugc = forms.CharField(disabled=True)

