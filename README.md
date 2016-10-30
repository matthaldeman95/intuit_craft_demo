# intuit_craft_demo
Craft demo for Intuit interview - Applications Operations Engineer

A Django web application that continuously monitors the availability and load time of the websites:

      https://turbotax.intuit.com/?cid=seq_intuit_tt_click_hd
      https://en.wikipedia.org/wiki/Intuit
      
Features:
- Collects site availability and load time every minute
- Tables and plots display site load times over user configurable time ranges
- If a site is unavailable, an email is sent to myself with the HTTP error code

### Directions

#### Dependencies:

- python 2.7

- pip

- virtualenv

            $ sudo pip install virtualenv

- matplotlib - Matplotlib has many dependency that may cause this app to fail.  These dependencies include
    plotly and freetype (which may require a brew installation rather than pip).
    [http://matplotlib.org/1.5.1/users/installing.html#required-dependencies](Check here if there are
    dependency issues installing matplotlib.)

    On Linux:

            $ sudo apt-get install python-matplotlib

    On Mac:

            $ sudo pip install matplotlib

- django_tables2 - This is in the requirements.txt file but sometimes does not play nicely with it.

            $ sudo pip install django_tables2



All other dependencies should be handled by the requirements.txt file.

### Set up virtual environment and run development server

Clone or download this project, and cd into that directory.  Create a virtual environment and enter it:

            $ virtualenv venv
            $ source venv/bin/activate

Download and install all of the requirements:

            $ sudo pip install -r requirements.txt

Run the Django development server:

            $ python manage.py runserver

Using your favorite web browser, go to [127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard)
