from django.contrib.auth.models import User #gives you base user class
from django import forms 

from django.views.generic import View

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  
  class Meta: #information about your class
    model = User
    fields = ['username', 'email', 'password']
    

