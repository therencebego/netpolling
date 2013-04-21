from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url('^$', 'netpolling.iw.views.index'),
                       url(r'^index/$', 'netpolling.iw.views.index'),
                       url(r'^co/$', 'netpolling.iw.views.co'),
                       url(r'^manager/$', 'netpolling.iw.views.manager'),
                       url(r'^control/$', 'netpolling.iw.views.control', name="control"))
