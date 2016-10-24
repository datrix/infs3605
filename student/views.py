from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import student, StudentFilter, enrol, coopPlacement
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StudentForm, EnrolForm, coopPlacementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_bootstrap_calendar.models import CalendarEvent
from django_tables2 import RequestConfig
from .tables import StudentDetailTable, StudentTable, CoursesTakenTable, coopPrefTable
from django.core.urlresolvers import reverse
from django.forms import formset_factory
from django.db.models import Avg, Max, Min, Sum
from django.core.urlresolvers  import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Reset, Button, Row
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
  placement_pref = coopPrefTable(coopPlacement.objects.filter(zID = zID))
  return render(request, 'student/detail.html', {'Student': Student, 'student_consult': student_consult, 'placement_pref': placement_pref})

def courses_taken(request, zID):
  Student = get_object_or_404(student, pk = zID)
  course_taken = CoursesTakenTable(enrol.objects.filter(zID = zID))
  all_grades = enrol.objects.filter(zID = zID).aggregate(Avg('grade')).values()[0]
  return render(request, 'student/courses_taken.html', {'Student':Student, 'course_taken': course_taken, 'all_grades': all_grades})

class AddCourses(LoginRequiredMixin, CreateView):
  login_url = '/login/' 
  model = enrol
  template_name = 'student/enrol.html'
  form_class = EnrolForm
 
  def get_initial(self):
    return{"zID":self.kwargs.get("zID")}
  
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

class CoopPlacementPref(LoginRequiredMixin, CreateView):
  login_url = '/login/'
  model = coopPlacement
  template_name ='student/coopPlacementForm.html'
  form_class = coopPlacementForm 
  
  def get_initial(self):
    return{"zID":self.kwargs.get("zID")}

class UpdateCoopPlacement(LoginRequiredMixin, UpdateView):
  login_url = '/login/'
  model = coopPlacement
  template_name = 'student/coopPlacementForm.html'
  #fields = ['zID','firstPref', 'secondPref', 'thirdPref']
  form_class = coopPlacementForm
  def get_object(self, queryset=None):
    coopObj = coopPlacement.objects.get(zID=self.kwargs['zID'])
    return coopObj 
  
  #reverse to previous URL
  def get_success_url(self):
    zID = self.kwargs['zID']
    return reverse('detail', kwargs={'zID': zID})
    
  
  
  
  
  
  
  