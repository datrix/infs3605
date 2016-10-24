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
from reportlab.platypus import Table, TableStyle, Image, Paragraph
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor






#######################################################

def index(request):
  return HttpResponse("<h1>Report Homepage</h1>")

@login_required(login_url='/login/')
def consultations(request):
  queryset = CalendarEvent.objects.all().order_by('start')
  f = ConsultationFilter(request.GET, queryset=queryset)
  all_consultations = ConsultationTable(f.qs)
  RequestConfig(request, paginate={'per_page': 15}).configure(all_consultations)
  
  
  return render(request, 'consultationReport.html', {'all_consultations': all_consultations, 'filter':f })


@login_required(login_url='/login/')
def students(request):
  queryset = student.objects.all().order_by('zID')
  f = StudentFilter(request.GET, queryset=queryset)
  all_students = StudentTable(f.qs)
  RequestConfig(request, paginate = {'per_page':25}).configure(all_students)
  
      ################################################################

    #styles = getSampleStyleSheet()
    #style = styles["BodyText"]
    
  
  
  if 'pdf' in request.GET:
    response = HttpResponse(content_type='application/pdf')
#    today = date.today()
 #   filename = 'pdf_demo' + today.strftime('%Y-%m-%d')
    response['Content-Disposition'] = 'filename="list_of_students.pdf"'
  #  response.write(pdf)

    width, height = A4
  
  
    def coord(x,y,unit = 1):
      x,y = x * unit, height - y * unit
      return x,y
    
    p = canvas.Canvas(response) #leave this here
    
    elements = []
    styles=getSampleStyleSheet()
    styleN = styles["Normal"]
    
    ################### Heqader Text ######################
    p.setFont('Helvetica', 18, leading=None)
    p.drawCentredString(300, 762.5, "Reports")
    UNSWLogo = ImageReader('http://web.maths.unsw.edu.au/~zdravkobotev/UNSW_logo.jpg')  
    p.drawImage(UNSWLogo, 60, 750, width=158.01, height=40)
    blackVerLine = ImageReader('report/images/bar.png')
    p.drawImage(blackVerLine, 245, 745, width=0.2, height=45)
    blackHorLine = ImageReader('http://www.circleoflifecoalition.org/wp-content/uploads/2014/09/horizontal-line-jpg-150x131.gif')
    p.drawImage(blackHorLine, 50, 730, width=485, height=10)
    
    ######### Beginning details #########################
    p.setFont('Helvetica', 8, leading=None)
    p.drawString(70, 720, "Results for:")
    p.drawString(120, 720, "Students")
    
    searchTerm = f
    p.drawCentredString(150, 700, str(searchTerm))
    
     
    
#    title = [['zID', 'First Name', 'Last Name', 'Email', 'Degree Code', 'Start Year']]
    

  
    #  ["zID", "First Name", "Last Name","Email", "Degree Code", "Start Year"],
      
      
    #  [[str(my_data.zID), str(my_data.f_name), str(my_data.l_name), str(my_data.email),
    #         str(my_data.degreeCode), str(my_data.startYear)] for my_data in f]]
    # , took out this so we can make the table fit for now.
    
    ############## Column Headings ##############
    col1 = Paragraph("<para align=center>zID</para>",styles['Normal'])
    col2 = Paragraph("<para align=center>First Name</para>",styles['Normal'])
    col3 = Paragraph("<para align=center>Last Name</para>",styles['Normal'])
    col4 = Paragraph("<para align=center>Email</para>",styles['Normal'])
    col5 = Paragraph("<para align=center>Degree</para>",styles['Normal'])
    col6 = Paragraph("<para align=center>Start Year</para>",styles['Normal'])
    
    data = [[col1, col2, col3, col4, col5, col6]]
    t1 = Table(data)
    t1.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,-1),2, colors.white),
                          ('LINEBELOW', (0,0), (-1,-1), 2, colors.white),
                          ('ROWBACKGROUNDS', (0,0), (-1,-1), [(colors.black), colors.black]),
                          ('FONTSIZE', (0,0), (-1,-1), 8)]))
    
    t1.wrapOn(p, width, height)
    t1.drawOn(p, *coord(2,15,cm))
    
    
    
    
    ################## data ######################
    data = [[str(my_data.zID), str(my_data.f_name), str(my_data.l_name), 
    str(my_data.email), str(my_data.degreeCode), str(my_data.startYear)] for my_data in f]
    t = Table(data)
    t.setStyle(TableStyle([('LINEABOVE',(0,0),(-1,-1),2, colors.white),
                           ('LINEBELOW', (0,0), (-1,-1), 2, colors.white),
                           ('ROWBACKGROUNDS', (0,0), (-1,-1), [HexColor('#e7eff8'), HexColor('#f6f9fc')]),
                           ('FONTSIZE', (0,0), (-1,-1), 8)]))
    t.wrapOn(p, width, height)
    t.drawOn(p, *coord(1.5,12,cm))
    
     ######count figure######
    dataCount = len(data)      
    p.setFont('Helvetica', 8, leading=None)    
    p.drawCentredString(450, 720, "No. of Results:")
    p.drawCentredString(500,720, str(dataCount))
       
    
    
   
    ########## Footer ############
    p.drawImage(blackHorLine, 50, 60, width=485, height=10)
    p.setFont('Helvetica', 6, leading=None)
    p.drawCentredString(100, 55, "UNSW UGC System Student Report")
    
    page_number = p.getPageNumber()
    p.drawCentredString(520, 55, "Page ")
    p.drawCentredString(530, 55, str(page_number))

    
          
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



  