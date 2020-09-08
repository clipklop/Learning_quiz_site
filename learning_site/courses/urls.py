from django.urls import path, re_path
from django.conf.urls import url


from . import views

app_name = 'courses'

urlpatterns = [
    # path('', views.hello_world),
    re_path(r'^$', views.course_list, name='list'),
    re_path(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$',
        views.step_detail, name='step'),
    re_path(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
