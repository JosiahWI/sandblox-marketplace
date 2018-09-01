"""
WSGI config for sandbloxmarketplace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'sandbloxmarketplace/'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandbloxmarketplace.settings")

application = get_wsgi_application()
