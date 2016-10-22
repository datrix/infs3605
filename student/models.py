from __future__ import unicode_literals

from django.db import models
from course.models import course
from datetime import datetime
import django_filters
import datetime

year_dropdown = []
for y in range(2011, (datetime.datetime.now().year + 5)):
    year_dropdown.append((y, y))
    
semester_dropdown = [
  ('S1', ('Semester 1')),
  ('S2', ('Semester 2')),
]

# Create your models here.


class degree(models.Model):
  degreeCode = models.IntegerField(verbose_name='Degree Code', primary_key = True)
  degreeName = models.CharField(verbose_name='Degree', max_length = 200)
  
  def __str__(degree):
    return str(degree.degreeCode) + " - " + str(degree.degreeName)
  
class student(models.Model):
  zID = models.CharField(verbose_name=('zID'), max_length = 8, primary_key = True)
  f_name = models.CharField(verbose_name=('First Name'), max_length = 50)
  l_name = models.CharField(verbose_name=('Last Name'), max_length = 50)
  email = models.CharField(verbose_name=('E-mail Address'), max_length = 100)
  degreeCode = models.ForeignKey(degree, verbose_name=('Degree Code'),on_delete = models.CASCADE, null=True)
  startYear = models.IntegerField(verbose_name=('Year Started'))
  
  def getYear(self):
    return str(datetime.now().year - self.startYear)
  
  def __str__(self):
    return self.zID + ' - ' + self.f_name + ' ' + self.l_name
  
class enrol(models.Model):
  zID = models.ForeignKey(student, on_delete = models.CASCADE, null = True)
  course = models.ForeignKey(course, related_name = 'course_old', null = True)
  grade = models.IntegerField(verbose_name=('Grade'), null = True)
  sem_taken = models.CharField(verbose_name=('Semester'), choices=semester_dropdown, max_length = 20, null = True)
  year = models.IntegerField(verbose_name=('year'), choices=year_dropdown, default=datetime.datetime.now().year)
  
  def __str__(enrol):
    return str(enrol.zID) + '------- Previous Course: ' + str(enrol.course_old) + '------- Current Course: ' + str(enrol.course_new) 

  
class StudentFilter(django_filters.FilterSet):
  zID = django_filters.CharFilter(name='zID', lookup_expr = 'icontains')
  First_name = django_filters.CharFilter(name='f_name', lookup_expr = 'icontains')
  Last_name = django_filters.CharFilter(name='l_name', lookup_expr = 'icontains')
  email = django_filters.CharFilter(name='email', lookup_expr = 'icontains')
  Degree_code = django_filters.NumberFilter(name='degreeCode')
  Start_year = django_filters.RangeFilter(name='startYear')
  
  class Meta:
    model = student
    fields = ['zID']
    
