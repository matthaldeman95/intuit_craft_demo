from django.conf.urls import url

from . import views

app_name = 'intuit_site_check'
urlpatterns = [
    #/dashboard/
    url(r'^$', views.dashboard, name='dashboard'***REMOVED***,
    #/dashboard/refresh/
    url(r'refresh/$', views.refresh_site_data, name='refresh'***REMOVED***,
    #/dashboard/<site_id>/
    url(r'^(?P<site_id>[a-z***REMOVED***+***REMOVED***/$', views.detail_page, name='details'***REMOVED***
***REMOVED***