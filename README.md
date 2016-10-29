# intuit_craft_demo
Craft demo for Intuit interview - Applications Operations Engineer

A Django web application that continuously monitors the availability and load time of the websites:

      https://turbotax.intuit.com/?cid=seq_intuit_tt_click_hd
      https://en.wikipedia.org/wiki/Intuit
      
Features:
- Collects site availability and load time every minute
- Tables and plots display site load times over user configurable time ranges
- If a site is unavailable, an email is sent to myself with the HTTP error code

## Directions

Dependencies:

python 2.7


pip

matplotlib

    On Linux:

            $ sudo apt-get install python-matplotlib

    On Mac:

            $ sudo pip install matplotlib

django_tables2 - Doesn't seem to play nicely with the later requirements installation

            $ sudo pip install django_tables2

virtualenv

            $ sudo pip install virtualenv

All other dependencies should be handled by the requirements.txt file.

Clone or download this project, and cd into that directory.  Create a virtual environment and enter it:

            $ virtualenv venv
            $ source venv/bin/activate

Download and install all of the requirements:

            $ sudo pip install -r requirements.txt

Run the Django development server:

            $ python manage.py runserver

Using your favorite web browser, go to [127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard)
