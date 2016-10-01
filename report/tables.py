import django_tables2 as tables
from django_bootstrap_calendar.models import CalendarEvent


class ConsultationTable(tables.Table):
  edit_consultation = tables.TemplateColumn('<a href="/calendar/{{record.title}}" class = "glyphicon glyphicon-pencil"></a>', orderable=False)
  checkbox = tables.TemplateColumn('<input type="checkbox" value="{{ record.title }}" />', verbose_name="Checkbox", orderable=False)
  
  class Meta: 
    model = CalendarEvent
    exclude = ['notes', 'url']
    attrs = {'class': 'paleblue'}
    
    