from django.urls import path, re_path
from django.conf.urls import url


from . import views

app_name = 'courses'

urlpatterns = [
    re_path(r'^$', views.course_list, name='list'),
    re_path(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$',
        views.text_detail, name='text'),
    re_path(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$',
        views.quiz_detail, name='quiz'),
    re_path(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create, name='create_quiz'),
    re_path(r'(?P<course_pk>\d+)/edit_quiz/(?P<quiz_pk>\d+)/$',
        views.quiz_edit, name='edit_quiz'),
    re_path(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
