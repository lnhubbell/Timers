from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from timer import views

urlpatterns = patterns('',
    url(r'^timers/$', views.TimerList.as_view()),
    url(r'^timers/(?P<pk>[0-9]+)/$', views.TimerDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
