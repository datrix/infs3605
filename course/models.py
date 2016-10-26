from __future__ import unicode_literals

from django.db import models
import django_filters

# Create your models here.
class course (models.Model): 
  courseCode = models.CharField(max_length = 8, primary_key = True, verbose_name=('Course Code'))
  courseName = models.CharField(max_length = 50, verbose_name=('Description'))
  LIC_name = models.CharField(max_length = 50, verbose_name=('Lecturer in Charge'))
  LIC_email = models.CharField(max_length = 100, verbose_name=('LIC Email'))
  LIC_phone = models.IntegerField(verbose_name=('LIC Phone'))
  
  def __str__(self):
    return self.courseCode + ' - ' + self.courseName
  
class CourseFilter(django_filters.FilterSet):
  
  class Meta:
    model = course
    fields = ['courseCode']
