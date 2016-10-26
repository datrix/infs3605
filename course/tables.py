import django_tables2 as tables
from .models import course


class CourseTable(tables.Table):
  view = tables.TemplateColumn('<a href="/courses/{{record.courseCode}}" class = "glyphicon glyphicon-option-horizontal"></a>' , orderable=False)
  
  class Meta: 
    model = course
    template = 'django_tables2/bootstrap.html'
    attrs = {'class': 'table table-bordered table-striped table-hover'}

    