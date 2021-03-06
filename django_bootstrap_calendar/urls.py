# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import include, url
#from django.conf.urls import patterns, url
from django_bootstrap_calendar import views
from views import CalendarJsonListView, CalendarView
from .views import CreateEvent, EditEvent, DeleteEvent, CreateEventStudent, AddNotes, alerts
from . import views

"""
urlpatterns = patterns('django_bootstrap_calendar.views',
                       url(r'^json/$', CalendarJsonListView.as_view(),name='calendar_json'),
                       url(r'^$',CalendarView.as_view(),name='calendar'),
                       url(r'^newevent$', CreateEvent.as_view(success_url="/calendar/"), name='newevent' ),
                       url(r'^(?P<title>[\s\S]*)/edit$', EditEvent.as_view(success_url="/calendar/"), name='editEvent'),
                       url(r'^(?P<title>[\s\S]*)$',views.detail, name = 'detail'),
                       
                      )
"""

urlpatterns = [
    url(r'^json/$', CalendarJsonListView.as_view(),name='calendar_json'),
    url(r'^$',CalendarView.as_view(),name='calendar'),
    url(r'^alerts$', views.alerts, name = 'alerts'),
    url(r'^newevent$', CreateEvent.as_view(success_url="/calendar/"), name='newevent' ),
    url(r'^newevent_newstudent$', CreateEventStudent.as_view(success_url="/calendar/"), name='newevent_newstudent' ),
    url(r'^(?P<title>[\s\S]*)/edit/$', EditEvent.as_view(), name='editEvent'),
    url(r'^(?P<title>[\s\S]*)/add_notes/$', AddNotes.as_view(), name='editEvent'),  
    url(r'^(?P<title>[\s\S]*)/delete/$', DeleteEvent.as_view(success_url="/calendar/"), name='deleteEvent'),
    url(r'^(?P<title>[\s\S]*)$',views.eventTable, name = 'detail'),
]