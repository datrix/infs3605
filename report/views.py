from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django_bootstrap_calendar.models import CalendarEvent
from student.models import student, StudentFilter
from django.contrib.auth.decorators import login_required
from .tables import ConsultationTable, StudentTable
from django_tables2 import RequestConfig, SingleTableView

import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.lib.units import cm

def index(request):
  return HttpResponse("<h1>Report Homepage</h1>")

@login_required(login_url='/login/')
def consultations(request):
  table = ConsultationTable(CalendarEvent.objects.all(), order_by= 'start')
  RequestConfig(request, paginate={'per_page': 15}).configure(table)
  return render(request, 'consultationReport.html', {'all_consultations': table })


@login_required(login_url='/login/')
def students(request):
  queryset = student.objects.all().order_by('zID')
  f = StudentFilter(request.GET, queryset=queryset)
  all_students = StudentTable(f.qs)
  RequestConfig(request, paginate = {'per_page':25}).configure(all_students)
  
  if 'pdf' in request.GET:
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="list_of_students.pdf"'

    width, height = A4
    
    def coord(x,y,unit = 1):
      x,y = x * unit, height - y * unit
      return x,y
    
    p = canvas.Canvas(response)
  
    
    data = [[str(my_data.zID)] for my_data in f]
    
    t = Table(data)
    t.wrapOn(p, width, height)
    t.drawOn(p, *coord(2,5,cm))

      # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
  
  return render(request, 'studentReport.html', {'all_students': all_students, 'filter':f})

#class students(TemplateView):
#  template_name = "studentReport.html"
#  
#  def get_queryset(self, **kwargs):
#    return student.objects.all()
#   
#  def get_context_data(self, **kwargs):
#    context = super(students, self).get_context_data(**kwargs)
#    table = StudentTable
#    RequestConfig(self.request).configure(table)
#    context['table'] = table
#    return context

  