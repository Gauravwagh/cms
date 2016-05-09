from django.conf.urls import patterns, include, url
from django.contrib import admin
from whatever import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'whatever.views.whatever'),
    url(r'^add/$', 'whatever.views.add'),
)
