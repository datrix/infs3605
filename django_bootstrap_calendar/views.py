# -*- coding: utf-8 -*-
__author__ = 'sandlbn and w3lly'

from django.views.generic import ListView, TemplateView
from models import CalendarEvent
from serializers import event_serializer
from utils import timestamp_to_datetime
from .forms import EventForm, addNotes #new event form 
from django.views.generic import View #view new event form -- (don't think we need this)
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import CalendarEvent, apptType
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta, time
from .tables import EventTable 
from student.models import student
from student.forms import StudentForm
from django_tables2 import SingleTableView, RequestConfig
from django.core.urlresolvers import reverse
from django.db.models import Count

### ReportLab
import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Image, Paragraph, SimpleDocTemplate, Spacer
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
  
class CalendarJsonListView(ListView):

    template_name = 'django_bootstrap_calendar/calendar_events.html'
    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date),# + datetime.timedelta(-30),
                    timestamp_to_datetime(to_date)
                    )
            )
        elif from_date:
            queryset = queryset.filter(
                start__gte=timestamp_to_datetime(from_date)
            )
        elif to_date:
            queryset = queryset.filter(
                end__lte=timestamp_to_datetime(to_date)
            )
        return event_serializer(queryset)
    

class CalendarView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    #redirect_field_name = 'redirect_to'
    template_name = 'django_bootstrap_calendar/calendar.html'
    model = CalendarEvent

    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
            
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        context['high_priority_count'] = CalendarEvent.objects.filter(css_class="event-important").filter(start__gte=today_start).filter(start__lt=today_end).count()
        context['cred_trans_count'] = CalendarEvent.objects.filter(apptType="Credit Transfer").filter(start__gte=today_start).count()
        context['int_exch_count'] = CalendarEvent.objects.filter(apptType="International Exchange").filter(start__gte=today_start).count()
        context['consult_today'] = CalendarEvent.objects.filter(start__gte=today_start).filter(start__lt=today_end).order_by('start')
        return context

class CreateEvent(LoginRequiredMixin, CreateView): 
    login_url = '/login/'
    model = CalendarEvent
    template_name = 'calendarevent_form.html'
    form_class = EventForm
    
    def get_initial(self):
      return{"zID":self.kwargs.get("zID")}
          
class CreateEventStudent(LoginRequiredMixin, CreateView): 
    login_url = '/login/'
    model = CalendarEvent, student
    template_name = 'calendarevent_form_new.html'
    form_class = EventForm# StudentForm}
    
class EditEvent(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = EventForm
    model = CalendarEvent 
    #fields = ['title', 'css_class', 'start', 'end', 'zID', 'apptType', 'ugc']
    template_name= 'editEvent.html'
      
    def get_object(self, queryset=None):
      eventObj = CalendarEvent.objects.get(pk=self.kwargs['title'])
      return eventObj
    
    def get_success_url(self):
      title = self.kwargs['title']
      return reverse('detail', kwargs={'title': title})
        
    def eventDetails(request, title):  
      Consultation = get_object_or_404(CalendarEvent, pk=title)
      calendar_events = eventDetails(CalendarEvent.objects.filter(title=title))
    
      return render(request,'editEvent.html', {'Consultation':Consultation})
       
class AddNotes(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = addNotes
    model = CalendarEvent, student
    template_name= 'addNotes.html'
  
      
    def get_object(self, queryset=None):
      eventObj = CalendarEvent.objects.get(pk=self.kwargs['title'])
      return eventObj
    
    def get_success_url(self):
      title = self.kwargs['title']
      return reverse('detail', kwargs={'title': title})
    
class DeleteEvent(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = CalendarEvent
    success_url = 'index'
    template_name = 'deleteEvent.html'
    
    def get_object(self, queryset=None):
      eventObj = CalendarEvent.objects.get(pk=self.kwargs['title'])
      return eventObj
    
def eventTable(request, title):  
    Consultation = get_object_or_404(CalendarEvent, pk=title)
    
    calendar_events = EventTable (CalendarEvent.objects.filter(title = title))
    calendar_events.paginate(page=request.GET.get('page', 1), per_page=15)
    
    
    if 'pdf' in request.GET:
        pdf_name = "%s.pdf" % str(Consultation.title)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=%s' % pdf_name

        p = canvas.Canvas(response)

        doc = SimpleDocTemplate(response, rightMargin=2*cm, leftMargin=2*cm, topMargin=0.3 * cm, bottomMargin=0)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name="TableHeader", fontSize=11, alignment=TA_CENTER,
            fontName="Helvetica"))    
        styles.add(ParagraphStyle(
            name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,
            fontName="FreeSansBold"))
        styles.add(ParagraphStyle(
            name="Justify", alignment=TA_JUSTIFY, fontName="FreeSans"))

        #elements append
        elements = []
        UNSWLogo = Image('report/images/pdfheader.PNG')
        UNSWLogo.drawHeight = 4*cm
        UNSWLogo.drawWidth = 21 *cm
        
        head_s = Spacer(1, 1*cm)
        s = Spacer(1, 0.25*cm)
        
        elements.append(UNSWLogo)
        elements.append(head_s)
        header = (Paragraph(Consultation.title,styles['Heading1']))
        elements.append(header)
        elements.append(s)
        elements.append(Paragraph("Student: ", styles['Heading3']))
        elements.append(Paragraph("%s" % Consultation.zID,styles['Normal']))
        elements.append(Paragraph("Appointment Type: ", styles['Heading3']))
        elements.append(Paragraph("%s" % Consultation.apptType,styles['Normal']))
        elements.append(Paragraph("Start Time: ", styles['Heading3']))
        elements.append(Paragraph("%s" % Consultation.start,styles['Normal']))
        elements.append(Paragraph("End Time: ", styles['Heading3']))
        elements.append(Paragraph(str(Consultation.end),styles['Normal']))
        elements.append(Paragraph("Coordinator: ", styles['Heading3']))
        elements.append(Paragraph(Consultation.ugc,styles['Normal']))
        elements.append(Paragraph("Notes: ", styles['Heading3']))
        elements.append(Paragraph(Consultation.notes,styles['Normal']))

        doc.build(elements, onFirstPage=addPageNumber, onLaterPages=addPageNumber)
        return response

    return render(request, 'consultation.html', {'Consultation':Consultation})
  
  


def alerts(request):
  today = datetime.now().date()
  tomorrow = today + timedelta(1)
  today_start = datetime.combine(today, time())
  today_end = datetime.combine(tomorrow, time())
  
  qs_high_priority = CalendarEvent.objects.filter(css_class="event-important").filter(start__gte=today_start).filter(start__lt=today_end)
  qs_cred_trans = CalendarEvent.objects.filter(apptType="Credit Transfer").filter(start__gte=today_start)
  qs_int_exch = CalendarEvent.objects.filter(apptType="International Exchange").filter(start__gte=today_start)
  
  high_priority = EventTable(qs_high_priority, prefix='1-')
  cred_trans = EventTable(qs_cred_trans, prefix='2-')
  int_exch = EventTable(qs_int_exch, prefix='3-')
        
  RequestConfig(request, paginate={'per_page': 15}).configure(high_priority)
  RequestConfig(request, paginate={'per_page': 15}).configure(cred_trans)
  RequestConfig(request, paginate={'per_page': 15}).configure(int_exch)
  
  return render(request, 'alerts.html', {'high_priority': high_priority, 'cred_trans': cred_trans,'int_exch': int_exch})

def addPageNumber(canvas, doc):
    """
    Add the page number
    """
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.drawRightString(200*mm, 20*mm, text)
