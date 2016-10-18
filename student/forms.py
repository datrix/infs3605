from django import forms
from django.views.generic import View
from .models import student
from .models import degree
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Reset, Button, Row
from crispy_forms.bootstrap import InlineField, FormActions, InlineRadios

import django_filters

class StudentForm(forms.ModelForm):

  
  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Fieldset(
        'Use one or more of the following fields to filter through students:',
        'zID',
        
        Div(
          Div('f_name', css_class='col-md-5'),
          Div(css_class = 'col-md-1'),
          Div('l_name', css_class='col-md-5'),
          css_class='row',
        ),
        'email',
        'startYear',
        'degreeCode',
      ),
      
      ButtonHolder(
        Submit('submit', 'Submit', css_class='button white')
      )
    )
    
  class Meta: #information about the class
    model = student
    exclude = ['ugc', 'url']
    
    