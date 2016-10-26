from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courseTable, name = 'table'),  #homepage for courses
    url(r'(?P<courseCode>[\S]*)/$', views.course_detail, name='details')
]