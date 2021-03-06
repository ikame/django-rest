from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import urest
urest.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(urest.site.urls)),
)
