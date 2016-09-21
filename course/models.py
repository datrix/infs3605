from __future__ import unicode_literals

from django.db import models

# Create your models here.
class course (models.Model): 
  courseCode = models.CharField(max_length = 8, primary_key = True)
  courseName = models.CharField(max_length = 50)
  LIC_name = models.CharField(max_length = 50)
  LIC_email = models.CharField(max_length = 100)
  LIC_phone = models.IntegerField()
  
  def __str__(self):
    return self.courseCode + ' - ' + self.courseName