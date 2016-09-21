from django.http import HttpResponse 
from django.template import loader
from .models import course

def index(request):
  all_courses = course.objects.all()
  return HttpResponse("<h1>Course Homepage</h1>")
