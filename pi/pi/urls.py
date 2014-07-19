# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin

from pi.views import *
from books import views



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url('^$',hello),
    # url(r'^blog/', include('blog.urls')),
    url('^admin/',include(admin.site.urls)),
    url('^hello/$',hello),
    url('^time/$',current_datetime),
    url('^temperature/$',getCPUtemperature),
    url('^check/year/(.*)/$',check_year),
    url('^led/(.*)/$',ledset),
    url('^display/$',display_meta),

    url('^search/$', views.search),
)
