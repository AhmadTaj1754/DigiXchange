"""
WSGI config for modelproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject.settings')

#To avoid this problem, use mod_wsgi’s daemon mode with each site in
# its own daemon process, or override the value from the environment by
# enforcing os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings" in your
# # wsgi.py.
#
# os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

application = get_wsgi_application()
