import django_tables2 as tables
from django_bootstrap_calendar.models import CalendarEvent


class ConsultationTable(tables.Table):
  class Meta: 
    model = CalendarEvent
    exclude = ['notes', 'url']
    attrs = {'class': 'paleblue'}
    
    