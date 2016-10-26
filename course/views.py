from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.template import loader
from .models import course, CourseFilter
from .tables import CourseTable
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

@login_required(login_url='/login/')
def course_detail(request, courseCode):
  courseDetail = get_object_or_404(course, pk = courseCode)
  return render(request, 'course_detail.html', {'courseDetail': courseDetail})
  

#all courses table
@login_required(login_url='/login/')
def courseTable(request):
    queryset = course.objects.all().order_by('courseCode')
    f = CourseFilter(request.GET, queryset=queryset)
    course_table = CourseTable(f.qs)
    RequestConfig(request, paginate = {'per_page':15}).configure(course_table)
    return render(request, 'course_table.html', {'course_table': course_table, 'filter':f })
