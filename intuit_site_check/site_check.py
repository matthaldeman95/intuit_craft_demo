import requests
import compose_email

def site_check(url***REMOVED***:
    ***REMOVED***
    Checks if website is operational and returns data about connection
    :param url: URL of website to check
    :return:
        http_code:      HTTP code returned
        load_time:      Website load time
        email_sent:     Boolean stating whether an email was successfully sent.  False by
                             default, since no email is sent if website is working
    ***REMOVED***
    r = requests.get(url***REMOVED***
    http_code = r.status_code
    email_sent = False
    if http_code != requests.codes.ok:
        ***REMOVED***
            compose_email('Intuit Wikipedia Page', http_code, datetime.datetime.now(***REMOVED******REMOVED***
            email_sent = True
        ***REMOVED***
            pass

    load_time = r.elapsed.total_seconds(***REMOVED***

    return http_code, load_time, email_sent