from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^$', 'cms.views.upload_file'),
                       url(r'^employee/$', 'cms.views.list'),
                       url(r'^report/$', 'cms.views.report'),
                       url(r'^export/$', 'cms.views.export'),
                       )
