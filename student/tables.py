import django_tables2 as tables
from .models import student


class StudentTable(tables.Table):
  edit_student = tables.TemplateColumn('<a href="/student/{{record.zID}}" class = "glyphicon glyphicon-pencil"></a>', orderable=False)
  checkbox = tables.TemplateColumn('<input type="checkbox" value="{{ record.title }}" />', verbose_name="Checkbox", orderable=False)
  
  class Meta: 
    model = CalendarEvent
    attrs = {'class': 'paleblue'}
    
    