from .base import *

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='rM7BzieZZCB2Sjt5k7wxEgGVXUDt9dEomyUUIVmAQpkpwg8j30lEyDRAOchdYAHW')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ['django_extensions']

# FUNCTIONAL TESTS
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ['deleteme.functional_tests']

# django_admin_env_notice
# ------------------------------------------------------------------------------
ENVIRONMENT_NAME = "Development"
ENVIRONMENT_COLOR = "#8E8E8E"

# TEST APP
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['deleteme.test_app']

# Your stuff...
# ------------------------------------------------------------------------------
