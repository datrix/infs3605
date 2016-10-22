from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),  #homepage for reports
    url(r'^consultations$', views.consultations, name = 'consultations'),
    url(r'^students', views.students, name = 'students'),
]