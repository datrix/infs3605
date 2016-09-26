from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django_bootstrap_calendar.models import CalendarEvent
from django.contrib.auth.decorators import login_required
from .tables import ConsultationTable
from django_tables2 import RequestConfig


def index(request):
  return HttpResponse("<h1>Report Homepage</h1>")

@login_required(login_url='/login/')
def consultations(request):
  table = ConsultationTable(CalendarEvent.objects.all())
  RequestConfig(request).configure(table)
  context={
    'all_consultations': table
  }
  return render(request, 'consultationReport.html', context)
