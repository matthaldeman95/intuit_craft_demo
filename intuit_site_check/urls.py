from django.conf.urls import url
from . import views
from django.views.generic import RedirectView


app_name = 'intuit_site_check'
urlpatterns = [
    # /
    url(r'^$', RedirectView.as_view(url='dashboard')),
    # /dashboard/
    url(r'^dashboard/$', views.dashboard),
    # /dashboard/<site_id>/
    url(r'^(?P<site_id>[a-z]+)/$', views.detail_page, name='details')
]
