from __future__ import unicode_literals

from django.db import models
from course.models import course
from datetime import datetime

# Create your models here.
class student(models.Model):
  zID = models.CharField(max_length = 8, primary_key = True)
  f_name = models.CharField(verbose_name=('First Name'), max_length = 50)
  l_name = models.CharField(verbose_name=('Last Name'), max_length = 50)
  email = models.CharField(verbose_name=('E-mail Address'), max_length = 100)
  degree = models.CharField(verbose_name=('Degree'), max_length = 100)
  startYear = models.IntegerField(verbose_name=('Year Started'))
  
  def getYear(self):
    return str(datetime.now().year - self.startYear)
  
  def __str__(self):
    return self.zID + ' - ' + self.f_name + ' ' + self.l_name
  
#class enrol(models.Model):
 # zID = models.ForeignKey(student, on_delete = models.CASCADE)
  #course_old = models.ForeignKey('course.courseCode')
  
  
class enrol(models.Model):
  zID = models.ForeignKey(student, on_delete = models.CASCADE, null = True)
  course_old = models.ForeignKey(course, related_name = 'course_old', null = True)
  course_new = models.ForeignKey(course, related_name = 'course_new', null = True)    

  
  def __str__(enrol):
    return str(enrol.zID) + '------- Previous Course: ' + str(enrol.course_old) + '------- Current Course: ' + str(enrol.course_new)