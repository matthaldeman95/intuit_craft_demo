import requests
import compose_email
from .models import DataPoint, WebSite
import datetime


def site_check(WebSite***REMOVED***:
    ***REMOVED***
    Checks if website is operational and returns data about connection
    :param WebSite      Instance of a WebSite object that should be tested
    :return:
        http_code:      HTTP code returned
        load_time:      Website load time
        email_sent:     Boolean stating whether an email was successfully sent.  False by
                             default, since no email is sent if website is working
    ***REMOVED***
    site_name = WebSite.site_name
    url = WebSite.site_url
    email_sent = False

    # Try to download site data
    ***REMOVED***
        r = requests.get(url***REMOVED***
        http_code = r.status_code
        load_time = r.elapsed.total_seconds(***REMOVED***

    # Need to manually handle error 429, since it causes a requests error
    except requests.ConnectionError:
        http_code = 429
        load_time = 0

    # If http code is not (200***REMOVED***, it is an error.  Try to send an email
    if http_code != requests.codes.ok:
        # If the most recent error code is the same as the current one,
        # do not send an email - to prevent redundant emails every minute

        # If an email is sent unsuccessfully, there is no backup system currently
        codes = DataPoint.objects.all(***REMOVED***.filter(website=WebSite***REMOVED***.order_by('-timestamp'***REMOVED***
        most_recent_code = codes[0***REMOVED***.status_code
        if http_code != most_recent_code:
            ***REMOVED***
                compose_email.compose_email(site_name, http_code, datetime.datetime.now(***REMOVED******REMOVED***
                email_sent = True
            ***REMOVED***
                email_sent = False
        else:
            email_sent = True

    return http_code, load_time, email_sent
