***REMOVED***

import smtplib

username = 'matthaldeman95@gmail.com'
with open('/home/matthew/Documents/priv/pd.txt'***REMOVED*** as file:
    password = file.read(***REMOVED***

def compose_email(site_name, error_code, time***REMOVED***:
    Sends an email to myself when the site is down
    :param site_name:   Name of bad website
    :param error_code:  HTTP error code given
    :param time:        Time of bad request
    :return:
    sender = 'matthaldeman95@gmail.com'
    receiver = 'matthaldeman95@gmail.com'

    message =
    From:  Intuit <matthaldeman95@gmail.com>
    To:  System Administrator <matthaldeman95@gmail.com>
    MIME-Version: 1.0
    Content-type:  text/html
    Subject:  HTTP Error

    At %s, the following HTTP error occurred for the site %s:

    %s

    % (time, site_name, error_code***REMOVED***

    s = smtplib.SMTP('smtp.gmail.com:587'***REMOVED***
    s.ehlo(***REMOVED***
    s.starttls(***REMOVED***
    s.ehlo(***REMOVED***
    s.login(username, password***REMOVED***
    s.sendmail(sender, receiver, message***REMOVED***
***REMOVED***