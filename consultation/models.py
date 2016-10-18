from __future__ import unicode_literals

from django.db import models
#from apptType.models import apptType

class consultation(models.Model):
  cID = models.AutoField(primary_key = True)
  #title = model.CharField(max_length = 100)
  sTime = models.DateTimeField()
  fTime = models.DateTimeField()
  priority = models.CharField(max_length = 6, default = 'medium' )
  notes = models.CharField(max_length = 400)
  ugc = models.CharField(max_length = 100)

  def __str__(consultation):
    return str(consultation.cID) + ': ' + str(consultation.zID) #+ ' Date: ' + str(consultation.sTime) + ' - ' + str(consultation.fTime)
"""
class consultType(models.Model):
  cID = models.ForeignKey(consultation, on_delete = models.CASCADE, null = True)
  apptType = models.ForeignKey(apptType)
  
  def __str__(consultType): 
    return str(consultType.cID) + 'Consult Type: ' + str(consultType.apptType)
"""
