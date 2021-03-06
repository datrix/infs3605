import django_tables2 as tables
from django_bootstrap_calendar.models import CalendarEvent
from student.models import student


class ConsultationTable(tables.Table):
  view = tables.TemplateColumn('<a href="/calendar/{{record.title}}" class = "glyphicon glyphicon-pencil"></a>', orderable=False)
  delete = tables.TemplateColumn('<a href="/calendar/{{record.title}}/delete" class = "glyphicon glyphicon-trash"> </a>', orderable = False)
  
  class Meta: 
    model = CalendarEvent    
    template = 'django_tables2/bootstrap.html'
    exclude = ['notes', 'url']
    attrs = {'class': 'table table-bordered table-striped table-hover'}
    
    
class StudentTable(tables.Table):
  view = tables.TemplateColumn('<a href="/student/{{record.zID}}" class = "glyphicon glyphicon-pencil"></a>', orderable=False)
  delete = tables.TemplateColumn('<a href = "/student/{{record.zID}}/delete" class = "glyphicon glyphicon-trash"> </a>', orderable = False)
  
  class Meta:
    model = student
    template = 'django_tables2/bootstrap.html'
    attrs = {'class': 'table table-bordered table-striped table-hover'}
