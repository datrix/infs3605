from __future__ import unicode_literals

from django.db import models

class apptType (models.Model):
  apptType = models.CharField(max_length = 50, primary_key = True)
  apptDesc = models.CharField(max_length = 450)
  
  def __str__(self):
    return self.apptType + ' - ' + self.apptDesc