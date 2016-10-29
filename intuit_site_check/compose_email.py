import smtplib
from sys import platform

username = 'matthaldeman95@gmail.com'
try:
    if platform == "darwin":
        path = '/Users/Matt/Documents/priv/pd.txt'
    elif platform == "linux2":
        path = '/home/matthew/Documents/priv/pd.txt'
    with open(path) as pd_file:
        password = pd_file.read()
except:
    password = "filler password"


def compose_email(site_name, error_code, time):
    """
    Sends an email to myself when the site is down
    :param site_name:   Name of bad website
    :param error_code:  HTTP error code given
    :param time:        Time of bad request
    :return:
    """

    sender = 'matthaldeman95@gmail.com'
    receiver = 'matthaldeman95@gmail.com'

    message = """
    From:  Intuit <matthaldeman95@gmail.com>
    To:  System Administrator <matthaldeman95@gmail.com>
    MIME-Version: 1.0
    Content-type:  text/html
    Subject:  HTTP Error

    At %s, the following HTTP error occurred for the site %s:

    %s
    """ % (time, site_name, error_code)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(username, password)
    s.sendmail(sender, receiver, message)


if __name__ == "__main__":
    import datetime
    compose_email("test.com", 404, datetime.datetime.now())
