import requests
import compose_email
from .models import WebSite, DataPoint
import datetime

def site_check(WebSite***REMOVED***:
    ***REMOVED***
    Checks if website is operational and returns data about connection
    :param url: URL of website to check
    :return:
        http_code:      HTTP code returned
        load_time:      Website load time
        email_sent:     Boolean stating whether an email was successfully sent.  False by
                             default, since no email is sent if website is working
    ***REMOVED***
    url = WebSite.site_url
    email_sent = False

    ***REMOVED***
        r = requests.get(url***REMOVED***
        http_code = r.status_code
        load_time = r.elapsed.total_seconds(***REMOVED***

    except requests.ConnectionError:
        http_code = 429
        load_time = 0

    codes = DataPoint.objects.all(***REMOVED***.filter(website=WebSite***REMOVED***.order_by('-timestamp'***REMOVED***
    most_recent_code = codes[0***REMOVED***.status_code

    if http_code != requests.codes.ok:
        if http_code != most_recent_code:
            ***REMOVED***
                compose_email.compose_email('Intuit Wikipedia Page', http_code, datetime.datetime.now(***REMOVED******REMOVED***
                email_sent = True
            ***REMOVED***
                email_sent = False
        else:
            email_sent = True

    return http_code, load_time, email_sent
