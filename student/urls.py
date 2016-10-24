from django.conf.urls import url
from .views import CreateStudent, EditStudent, DeleteStudent, UpdateCourses, AddCourses, CoopPlacementPref, UpdateCoopPlacement
from django_bootstrap_calendar.views import CreateEvent
from . import views
from django_filters.views import FilterView
from .models import student, enrol

urlpatterns = [
    url(r'^$', views.index, name = 'index'),  #homepage
    url(r'^(?P<zID>z[0-9]{7})$', views.detail, name = 'detail'),
    url(r'^newStudent$', CreateStudent.as_view(success_url="/student/"), name='newStudent' ),
    url(r'^(?P<zID>z[0-9]{7})/edit/$', EditStudent.as_view(success_url="/student/"), name='student-update'),
    url(r'^(?P<zID>z[0-9]{7})/delete/$', DeleteStudent.as_view(success_url="/student/"), name='student-delete'),
    url(r'^(?P<zID>z[0-9]{7})/new_event/$', CreateEvent.as_view(success_url="/student/"), name='add-event'),
    url(r'^(?P<zID>z[0-9]{7})/courses_taken/$', views.courses_taken, name = 'courses_taken'),
    url(r'^(?P<zID>z[0-9]{7})/courses_taken/update/$', UpdateCourses.as_view(success_url="/r'^(?P<zID>z[0-9]{7})/courses_taken/$"), name='update-courses'), 
    url(r'^(?P<zID>z[0-9]{7})/courses_taken/addCourses/$', AddCourses.as_view(success_url="/student/"), name='add-courses'),
    url(r'^(?P<zID>z[0-9]{7})/co-op_pref/$', CoopPlacementPref.as_view(success_url="/student/"), name='co-op-pref'),
    url(r'^(?P<zID>z[0-9]{7})/update_co-op_pref/$', UpdateCoopPlacement.as_view(), name='co-op-pref_update'),
]