from django.contrib import admin
from .models import student
from .models import enrol
# Register your models here
admin.site.register(student)
admin.site.register(enrol)