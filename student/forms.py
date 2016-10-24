from django import forms
from django.views.generic import View
from .models import student
from .models import degree
from .models import enrol, coopPlacement
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Reset, Button, Row
from crispy_forms.bootstrap import InlineField, FormActions, InlineRadios
from django.forms.formsets import BaseFormSet
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

#cant fken make this look good, following link might work - rach
#https://kuanyui.github.io/2015/04/13/django-crispy-inline-form-layout-with-bootstrap/
import django_filters

class StudentForm(forms.ModelForm):
  
  ugc = forms.ModelChoiceField(queryset=User.objects.all())
  
  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Div('zID', 'f_name', 'l_name'),
        'email',
        'startYear',
        'degreeCode'  
    )
    
  class Meta: #information about the class
    model = student
    fields = ['zID', 'f_name', 'l_name',
              'email',
              'startYear',
              'degreeCode']
    exclude = ['ugc', 'url']
    
class EnrolForm (forms.ModelForm):  
  class Meta: 
    model = enrol 
    fields = ['zID', 'course', 'sem_taken', 'year', 'grade']
    
  def __init__(self, *args, **kwargs):
    super(EnrolForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Div('zID'),
      Div(
        Div('course', css_class="col-sm-5"),
        Div('sem_taken', css_class="col-sm-3"),
        Div('year', css_class="col-sm-2"),
        Div('grade', css_class="col-sm-2"),
        css_class = 'row'
      ),
       ButtonHolder(
      Submit('submit', 'Submit', css_class='button white')
       )
    )
 
  
class coopPlacementForm (forms.ModelForm):
    
  def __init__(self, *args, **kwargs):
    super(coopPlacementForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
       Div('zID'), 
        Div(
         Div('firstPref', css_class='col-md-4'),
          Div('secondPref', css_class='col-md-4'),
          Div('thirdPref', css_class='col-md-4'),
          css_class='row',
      ),
  ButtonHolder(
      Submit('submit', 'Submit', css_class='button white')
      )
    )
  
  class Meta: 
    model = coopPlacement
    fields = ['zID',  'firstPref', 'secondPref', 'thirdPref']
  
  
  
  
  
  
    