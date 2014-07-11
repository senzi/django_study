# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin

from pi.views import *



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url('^temperature/$', getCPUtemperature),
    url('^check/cpu/(\d{1,3})/$', check_cpu),
    url('^check/year/(.*)/$', check_year),
)
