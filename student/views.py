from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import student
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StudentForm #new event form 

# Create your views here.

def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def index(request):
    all_students = student.objects.all()
    context = {
      'all_students': all_students,
    }
    return render(request, 'student/index.html', context)
  
def detail(request, zID):
   Student = get_object_or_404(student, pk=zID)
   return render(request, 'student/detail.html', {'Student': Student,})
      
def get_event (request, calendar):
    return calendar.event_set.all()
  
class CreateStudent(CreateView):
  model = student
  template_name = 'student/createstudent_form.html'
  form_class = StudentForm
