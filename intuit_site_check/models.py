from __future__ import unicode_literals
from django.db import models


class WebSite(models.Model):
    """
    WebSite class.
    site_id:    Short name for website
    site_name:  Full text name of website
    site_url:   URL of site
    """
    site_id = models.CharField(max_length=25, default="site_id")
    site_name = models.CharField(max_length=25)
    site_url = models.URLField(max_length=200)

    def __str__(self):
        return self.site_name


class DataPoint(models.Model):
    """
    Class for each datapoint recorded
    website:        Site the point is associated with
    timestamp:      Time that point was recorded
    status_code:    HTML code given
    load_time       Time required for site load
    """
    website = models.ForeignKey(WebSite)
    timestamp = models.DateTimeField()
    status_code = models.IntegerField()
    load_time = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.website.site_id + ': ' + str(self.load_time)
