"""
WSGI config for intuit_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

if 'DYNO' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intuit_app.settings_heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intuit_app.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
