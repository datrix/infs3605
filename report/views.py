from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django_bootstrap_calendar.models import CalendarEvent, ConsultationFilter
from student.models import student, StudentFilter
from django.contrib.auth.decorators import login_required
from .tables import ConsultationTable, StudentTable
from django_tables2 import RequestConfig, SingleTableView

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Image, Paragraph, SimpleDocTemplate, Spacer
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing

styles = getSampleStyleSheet()









#######################################################

def index(request):
  return HttpResponse("<h1>Report Homepage</h1>")





@login_required(login_url='/login/')
def consultations(request):
  queryset = CalendarEvent.objects.all().order_by('start')
  f = ConsultationFilter(request.GET, queryset=queryset)
  all_consultations = ConsultationTable(f.qs)
  RequestConfig(request, paginate={'per_page': 15}).configure(all_consultations)
  
  if 'pdf' in request.GET:
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="list_of_consultations.pdf"'
      
    doc = SimpleDocTemplate(response, rightMargin=2*cm, leftMargin=2*cm, topMargin=0*cm, bottomMargin=0)
        
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TableHeader", fontSize=11, alignment=TA_CENTER,
        fontName="Helvetica"))    
    styles.add(ParagraphStyle(
        name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,
        fontName="FreeSansBold"))
    styles.add(ParagraphStyle(
        name="Justify", alignment=TA_JUSTIFY, fontName="FreeSans"))

    
   
    ########elements container########
    elements = []
    
    ###########header###############
    UNSWLogo = Image('report/images/pdfheader.PNG')
    UNSWLogo.drawHeight = 4*cm
    UNSWLogo.drawWidth = 21 *cm
   
    elements.append(UNSWLogo)
    s = Spacer(1, 0.2*cm)
    elements.append(s)
    
    #########title############
    title = """Reports by Consultations"""
    elements.append(Paragraph(title, styles['Heading2']))
    
    s = Spacer(1, 0.2*cm)
    elements.append(s)
    
    #p = Paragraph('''<para align=center spaceb=3> TITLE''')
       
    ############table header############
    header_Data = [[" Student ","Title","Staff", "Time"]]
    t1 = Table(header_Data,[6*cm, 7*cm, 2.25*cm, 3*cm])
    t1.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,-1),1, colors.black),
                            ('LINEBELOW',(0,0),(-1,-1),1, colors.black),
                            ('FONTSIZE', (0,0), (-1,-1), 8),
                            ('BACKGROUND',(0,0),(-1,-1), HexColor('#50A6C2'))]))
    elements.append(t1)
    s1 = Spacer(1, 0.1*cm)
    elements.append(s1)
    
    
    ######table data ##################
    table_data = [[ str(my_data.zID), str(my_data.title), str(my_data.ugc), str(my_data.start) ] for my_data in f]
    #'''str(my_data.apptType)'''
    t = Table(table_data,[6*cm, 7*cm, 2.25*cm, 3*cm])
    t.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,-1),2, colors.white),
                           ('LINEBELOW', (0,0), (-1,-1), 2, colors.white),
                           ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#e6f2ff'), HexColor('#c1e0ff')]),
                           ('FONTSIZE', (0,0), (-1,-1), 8)]))
    elements.append(t)
    
    
    ############footer##################
    '''pdffooter = Image('report/images/pdffooter.PNG')
    pdffooter.drawHeight = 1.5*cm
    pdffooter.drawWidth = 22 *cm
    s1 = Spacer(1, 20*cm)
    elements.append(s1)
    elements.append(pdffooter)'''


#    elements.append(t)
    doc.build(elements)
    return response
  
  
    #data = [[str(my_data.title), str(my_data.zID), str(my_data.ugc), str(my_data.apptType)] for my_data in f]  
    #data.append
  
  
  
  return render(request, 'consultationReport.html', {'all_consultations': all_consultations, 'filter':f })


@login_required(login_url='/login/')
def students(request):
  queryset = student.objects.all().order_by('zID')
  f = StudentFilter(request.GET, queryset=queryset)
  all_students = StudentTable(f.qs)
  RequestConfig(request, paginate = {'per_page':25}).configure(all_students)
  
      ################################################################
 
  if 'pdf' in request.GET:
    response = HttpResponse(content_type='application/pdf')
#    today = date.today()
 #   filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
    response['Content-Disposition'] = 'filename="list_of_students.pdf"'
  #  response.write(pdf)
  
    doc = SimpleDocTemplate(response, rightMargin=2*cm, leftMargin=2*cm, topMargin=0*cm, bottomMargin=0)
        
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TableHeader", fontSize=11, alignment=TA_CENTER,
        fontName="Helvetica"))    
    styles.add(ParagraphStyle(
        name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,
        fontName="FreeSansBold"))
    styles.add(ParagraphStyle(
        name="Justify", alignment=TA_JUSTIFY, fontName="FreeSans"))

    
   
    ########elements container########
    elements = []
    
    ###########header###############
    UNSWLogo = Image('report/images/pdfheader.PNG')
    UNSWLogo.drawHeight = 4*cm
    UNSWLogo.drawWidth = 21 *cm
   
    elements.append(UNSWLogo)
    s = Spacer(1, 0.2*cm)
    elements.append(s)
    
    #########title############
    title = """Reports by Students"""
    elements.append(Paragraph(title, styles['Heading2']))
    
    s = Spacer(1, 0.2*cm)
    elements.append(s)
    
    #p = Paragraph('''<para align=center spaceb=3> TITLE''')    
    ############table header############
    
    
    
    header_Data = [["zID","First Name","Last Name", "Email","Degree","Start Year"]]
    t1 = Table(header_Data,[1.5*cm,1.75*cm,2*cm,5*cm,7.75*cm,1.5*cm])
    t1.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,-1),1, colors.black),
                            ('LINEBELOW',(0,0),(-1,-1),1, colors.black),
                            ('FONTSIZE', (0,0), (-1,-1), 8),
                            ('INNERGRID',(0,0),(-1,-1),2,colors.black),
                            ('BACKGROUND',(0,0),(-1,-1), HexColor('#50A6C2'))]))
    elements.append(t1)
    s1 = Spacer(1, 0.1*cm)
    elements.append(s1)
    
    
    ######table data ##################
    table_data = [[str(my_data.zID), str(my_data.f_name), str(my_data.l_name), 
    str(my_data.email), str(my_data.degreeCode), str(my_data.startYear)] for my_data in f]
    #'''str(my_data.apptType)'''
    t = Table(table_data,[1.5*cm,1.75*cm,2*cm,5*cm,7.75*cm,1.5*cm])
              #,[6*cm, 7*cm, 2.25*cm, 3*cm])
    t.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,-1),2, colors.white),
                           ('LINEBELOW', (0,0), (-1,-1), 2, colors.white),
                           ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#e6f2ff'), HexColor('#c1e0ff')]),
                           ('FONTSIZE', (0,0), (-1,-1), 8)]))
    elements.append(t)
    
    
    ############footer##################
    '''pdffooter = Image('report/images/pdffooter.PNG')
    pdffooter.drawHeight = 1.5*cm
    pdffooter.drawWidth = 22 *cm
    s1 = Spacer(1, 20*cm)
    elements.append(s1)
    elements.append(pdffooter)'''


#    elements.append(t)
    doc.build(elements)
    return response

  return render(request, 'studentReport.html', {'all_students': all_students, 'filter':f})




  