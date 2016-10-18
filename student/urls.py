from django.conf.urls import url
from .views import CreateStudent, EditStudent, DeleteStudent
from . import views
from django_filters.views import FilterView
from .models import student, enrol

urlpatterns = [
    url(r'^$', views.index, name = 'index'),  #homepage
    url(r'^(?P<zID>z[0-9]{7})$', views.detail, name = 'detail'),
    url(r'^newStudent$', CreateStudent.as_view(success_url="/student/"), name='newStudent' ),
    url(r'^(?P<zID>z[0-9]{7})/edit/$', EditStudent.as_view(success_url="/student/"), name='student-update'),
    url(r'^(?P<zID>z[0-9]{7})/delete/$', DeleteStudent.as_view(success_url="/student/"), name='student-delete'),
    url(r'^(?P<zID>z[0-9]{7})/courses_taken/$', views.courses_taken, name = 'courses_taken'),
]