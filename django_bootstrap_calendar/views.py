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
from datetime import datetime, timedelta, time
from .tables import EventTable 
from student.models import student
from student.forms import StudentForm
#import datetime

from django.db.models import Count
  

  
class CalendarJsonListView(ListView):

    template_name = 'django_bootstrap_calendar/calendar_events.html'
    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date),# + datetime.timedelta(-30),
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
    model = CalendarEvent

    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
            
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        context['high_priority_count'] = CalendarEvent.objects.filter(css_class="event-important").filter(start__gte=today_start).filter(start__lt=today_end).count()
        context['cred_trans_count'] = CalendarEvent.objects.filter(apptType="Credit Transfer").filter(start__gte=today_start).filter(start__lt=today_end).count()
        context['int_exch_count'] = CalendarEvent.objects.filter(apptType="International Exchange").filter(start__gte=today_start).filter(start__lt=today_end).count()
        context['consult_today'] = CalendarEvent.objects.filter(start__gte=today_start).filter(start__lt=today_end)
        return context

class CreateEvent(LoginRequiredMixin, CreateView): 
    login_url = '/login/'
    model = CalendarEvent
    template_name = 'calendarevent_form.html'
    form_class = EventForm
    
class CreateEventStudent(LoginRequiredMixin, CreateView): 
    login_url = '/login/'
    model = CalendarEvent, student
    template_name = 'calendarevent_form_new.html'
    form_class = EventForm# StudentForm}
    


class EditEvent(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = EditEventForm
    #model = CalendarEvent 
    #fields = ['title', 'css_class', 'start', 'end', 'zID', 'apptType', 'ugc']
    template_name= 'editEvent.html'
      
    def get_object(self, queryset=None):
      eventObj = CalendarEvent.objects.get(pk=self.kwargs['title'])
      return eventObj
    
class DeleteEvent(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = CalendarEvent
    success_url = 'index'
    template_name = 'deleteEvent.html'
    
    def get_object(self, queryset=None):
      eventObj = CalendarEvent.objects.get(pk=self.kwargs['title'])
      return eventObj
    
def eventTable(request, title):  
    Consultation = get_object_or_404(CalendarEvent, pk=title)
    calendar_events = EventTable (CalendarEvent.objects.filter(title = title))
    calendar_events.paginate(page=request.GET.get('page', 1), per_page=15)
    return render(request, 'consultation.html', {'Consultation': Consultation, 'calendar_events':calendar_events})
    


  
#class CreateEvent(LoginRequiredMixin, EditView):
 #   login_url = '/login/'
  #  model = CalendarEvent
   # template_name = 'calendarevent_form.html'
    #form_class = EventForm
  


