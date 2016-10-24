from django.contrib import admin
from .models import student
from .models import enrol
from .models import degree, placementCompanies, coopPlacement
# Register your models here
admin.site.register(student)
admin.site.register(enrol)
admin.site.register(degree)
admin.site.register(coopPlacement)
admin.site.register(placementCompanies)
