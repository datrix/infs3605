from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django_bootstrap_calendar.models import CalendarEvent
from student.models import student
from django.contrib.auth.decorators import login_required
from .tables import ConsultationTable, StudentTable
from django_tables2 import RequestConfig


def index(request):
  return HttpResponse("<h1>Report Homepage</h1>")

@login_required(login_url='/login/')
def consultations(request):
  table = ConsultationTable(CalendarEvent.objects.all())
  RequestConfig(request).configure(table)
  return render(request, 'consultationReport.html', {'all_consultations': table })


@login_required(login_url='/login/')
def students(request):
  table = StudentTable(student.objects.all())
  return render(request, 'studentReport.html', {'all_students': table })
