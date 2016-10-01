from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import student
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StudentForm #new event form 
from django.contrib.auth.decorators import login_required
from django_bootstrap_calendar.models import CalendarEvent

# Create your views here.

@login_required(login_url='/login/')

def index(request):
    all_students = student.objects.all()
    context = {
      'all_students': all_students,
    }
    return render(request, 'student/index.html', context)
  
def detail(request, zID):
  Student = get_object_or_404(student, pk=zID)
  student_consult = CalendarEvent.objects.filter(zID = zID)
  return render(request, 'student/detail.html', {'Student': Student, 'student_consult': student_consult})
      
def get_event (request, calendar):
    return calendar.event_set.all()
  
class CreateStudent(CreateView):
  model = student
  template_name = 'student/createstudent_form.html'
  form_class = StudentForm
  

def student_list(request):
  student = StudentFilter(request.GET, queryset=student.objects.all())
  RequestConfig(request).configure(table)
  return render(request, 'student/student_filter.html', {'filter': student})