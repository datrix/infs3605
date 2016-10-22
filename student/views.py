from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import student, StudentFilter, enrol
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StudentForm, EnrolForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_bootstrap_calendar.models import CalendarEvent
from django_tables2 import RequestConfig
from .tables import StudentDetailTable, StudentTable, CoursesTakenTable
from django.core.urlresolvers import reverse
from django.forms import formset_factory

# Create your views here.

@login_required(login_url='/login/')

def index(request):
  queryset = student.objects.all()
  f = StudentFilter(request.GET, queryset=queryset)
  student_table = StudentTable(f.qs)
  RequestConfig(request, paginate = {'per_page':25}).configure(student_table)
  return render(request, 'student/index.html', {'student_table': student_table, 'filter':f})
  
def detail(request, zID):
  Student = get_object_or_404(student, pk=zID)
  student_consult = StudentDetailTable(CalendarEvent.objects.filter(zID = zID))
  return render(request, 'student/detail.html', {'Student': Student, 'student_consult': student_consult})

def courses_taken(request, zID):
  Student = get_object_or_404(student, pk = zID)
  course_taken = CoursesTakenTable(enrol.objects.filter(zID = zID))
  return render(request, 'student/courses_taken.html', {'Student':Student, 'course_taken': course_taken})

class AddCourses(LoginRequiredMixin, CreateView):
  login_url = '/login/'
  model = enrol 
  template_name = 'student/enrol.html'
  form_class = EnrolForm
  
  
class UpdateCourses(LoginRequiredMixin, UpdateView):
  login_url = '/login/'
  fields = ['zID', 'course', 'grade', 'sem_taken']
  template_name = 'student/editEnrolment.html'
  
  def get_object(self, queryset=None):
    enrolObj = enrol.objects.get(zID=self.kwargs['zID'])
    return enrolObj
      
def get_event (request, calendar):
    return calendar.event_set.all()
  
class CreateStudent(LoginRequiredMixin, CreateView):
  login_url = '/login/'
  model = student
  template_name = 'student/createstudent_form.html'
  form_class = StudentForm

class EditStudent(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    #model = student
    fields = ['zID','f_name', 'l_name', 'email', 'degreeCode', 'startYear']
    template_name = 'student/editStudent.html'
    
    def get_object(self, queryset=None):
      studentObj = student.objects.get(zID=self.kwargs['zID'])
      return studentObj  
  
class DeleteStudent(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = student
    success_url = 'index'
    template_name = 'student/deleteStudent.html'
    
    def get_object(self, queryset=None):
      studentObj = student.objects.get(zID=self.kwargs['zID'])
      return studentObj 
  
def student_list(request):
  student = StudentDetailTable(request.GET, queryset=student.objects.all())
  RequestConfig(request, paginate = {'per_page':25}).configure(student)
  return render(request, 'student/student_filter.html', {'filter': student})