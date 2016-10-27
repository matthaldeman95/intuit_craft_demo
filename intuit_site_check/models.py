from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

class WebSite(models.Model***REMOVED***:
    ***REMOVED***
    WebSite class.
    site_id:    Short name for website
    site_name:  Full text name of website
    site_url:   URL of site
    ***REMOVED***
    site_id = models.CharField(max_length=25, default="site_id"***REMOVED***
    site_name = models.CharField(max_length=25***REMOVED***
    site_url = models.URLField(max_length=200***REMOVED***
    on_error_message = models.BooleanField(default=False***REMOVED***

    def __str__(self***REMOVED***:
        return self.site_name

class DataPoint(models.Model***REMOVED***:
    ***REMOVED***
    Class for each datapoint recorded
    website:        Site the point is associated with
    timestamp:      Time that point was recorded
    status_code:    HTML code given
    load_time       Time required for site load
    ***REMOVED***
    website = models.ForeignKey(WebSite***REMOVED***
    timestamp = models.DateTimeField(***REMOVED***
    status_code = models.IntegerField(***REMOVED***
    load_time = models.DecimalField(max_digits=10, decimal_places=5***REMOVED***

    def __str__(self***REMOVED***:
        return self.website.site_id + ': ' + str(self.load_time***REMOVED***

    def timestamp_5_min(self***REMOVED***:
        return self.timestamp >= timezone.now(***REMOVED*** - datetime.timedelta(minutes=5***REMOVED***

