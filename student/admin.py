from django.contrib import admin
from .models import student
from .models import enrol
from .models import degree
# Register your models here
admin.site.register(student)
admin.site.register(enrol)
admin.site.register(degree)