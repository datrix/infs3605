import django_tables2 as tables
from .models import CalendarEvent 
from django_bootstrap_calendar.models import CalendarEvent 

class EventTable(tables.Table):
  selection = tables.CheckBoxColumn(accessor='id', orderable=False)
  view = tables.TemplateColumn('<a href="{{record.title}}" class = "glyphicon glyphicon-pencil"></a>', orderable=False)
  delete = tables.TemplateColumn('<a href = "{{record.title}}/delete" class = "glyphicon glyphicon-trash"> </a>', orderable = False)

  
  class Meta: 
    model = CalendarEvent
    template = 'django_tables2/bootstrap.html'
    attrs = {'class': 'table table-bordered table-striped table-hover'}
    
    