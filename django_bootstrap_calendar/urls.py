# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from views import CalendarJsonListView, CalendarView
from .views import CreateEvent
from . import views

urlpatterns = patterns('django_bootstrap_calendar.views',
                       url(r'^json/$', CalendarJsonListView.as_view(),name='calendar_json'),
                       url(r'^$',CalendarView.as_view(),name='calendar'),
                       url(r'^newevent$', CreateEvent.as_view(success_url="/calendar/"), name='newevent' ),
                       url(r'^(?P<title>[\s\S]*)$',views.detail, name = 'detail'),
                      )

