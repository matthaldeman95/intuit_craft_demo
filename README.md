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

pip
matplotlib
django_tables2
virtualenv

All other dependencies should be handled by pip later in the process.

Clone or download this repository, and cd into that directory.  Create a virtual environment and enter it:

            $ virtualenv venv
            $ source venv/bin/activate

Download all of the requirements:

            $ sudo pip install -r requirements.txt

Run the Django development server:

            $ python manage.py runserver

Using your favorite web browser, go to   127.0.0.1:8000/dashboard