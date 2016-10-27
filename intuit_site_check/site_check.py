import requests
import compose_email
from .models import WebSite

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
    r = requests.get(url***REMOVED***
    http_code = r.status_code
    email_sent = False
    load_time = r.elapsed.total_seconds(***REMOVED***
    # TODO Fix email, need password maintained privately?
    if http_code != requests.codes.ok:
        if not WebSite.on_error_message:
            ***REMOVED***
                compose_email('Intuit Wikipedia Page', http_code, datetime.datetime.now(***REMOVED******REMOVED***
                email_sent = True
                WebSite.on_error_message = True
            ***REMOVED***
                pass

    elif WebSite.on_error_message:
        WebSite.on_error_message = False

    return http_code, load_time, email_sent
