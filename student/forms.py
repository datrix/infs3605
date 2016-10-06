from django import forms
from django.views.generic import View
from .models import student
from .models import degree

import django_filters



class StudentForm(forms.ModelForm):
  class Meta:
    model = student
    fields = ['zID', 'f_name', 'l_name', 'email', 'startYear']
    
 