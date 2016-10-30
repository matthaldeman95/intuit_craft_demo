from django.conf.urls import url
from . import views
from django.http import HttpResponseRedirect


app_name = 'intuit_site_check'
urlpatterns = [
    # /
    url(r'^$', views.dashboard, name='index'),
    # /dashboard/
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # /dashboard/<site_id>/
    url(r'^(?P<site_id>[a-z]+)/$', views.detail_page, name='details')
]
