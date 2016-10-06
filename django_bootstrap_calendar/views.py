# -*- coding: utf-8 -*-
__author__ = 'sandlbn and w3lly'

from django.views.generic import ListView, TemplateView
from models import CalendarEvent
from serializers import event_serializer
from utils import timestamp_to_datetime
from .forms import EventForm, EditEventForm #new event form 
from django.views.generic import View #view new event form -- (don't think we need this)
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import CalendarEvent
from .models import apptType
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone


import datetime
  

  
class CalendarJsonListView(ListView):

    template_name = 'django_bootstrap_calendar/calendar_events.html'

    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date) + datetime.timedelta(-30),
                    timestamp_to_datetime(to_date)
                    )
            )
        elif from_date:
            queryset = queryset.filter(
                start__gte=timestamp_to_datetime(from_date)
            )
        elif to_date:
            queryset = queryset.filter(
                end__lte=timestamp_to_datetime(to_date)
            )
        return event_serializer(queryset)


class CalendarView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    #redirect_field_name = 'redirect_to'
    template_name = 'django_bootstrap_calendar/calendar.html'

class CreateEvent(LoginRequiredMixin, CreateView): 
    login_url = '/login/'
    model = CalendarEvent
    template_name = 'calendarevent_form.html'
    form_class = EventForm


class EditEvent(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = EditEventForm
    #model = CalendarEvent 
    #fields = ['title', 'css_class', 'start', 'end', 'zID', 'apptType', 'ugc']
    template_name= 'editEvent.html'
      
    def get_object(self, queryset=None):
      eventObj = CalendarEvent.objects.get(pk=self.kwargs['title'])
      
      return eventObj
    
def detail(request, title):  
    Consultation = get_object_or_404(CalendarEvent, pk=title)
    return render(request, 'consultation.html', {'Consultation': Consultation,})
    

#class CreateEvent(LoginRequiredMixin, EditView):
 #   login_url = '/login/'
  #  model = CalendarEvent
   # template_name = 'calendarevent_form.html'
    #form_class = EventForm
  


