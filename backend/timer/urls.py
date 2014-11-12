from django.conf.urls import patterns, url
from timer import views

urlpatterns = patterns('',
    url(r'^timers/$', views.TimerList.as_view()),
    url(r'^timers/(?P<pk>[0-9]+)/$', views.TimerDetail.as_view()),
)
