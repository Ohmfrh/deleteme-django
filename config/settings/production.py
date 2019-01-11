from .base import *

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY', default='aKQIdaR10umIgVZQfF5DOPhGwqlpDwwvNGytsfPhBqqTpJwoX0bErKvtPgev79TR')

DEBUG = False

ALLOWED_HOSTS = ['*']

# TEST APP
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['deleteme.test_app']

# django_admin_env_notice
# ------------------------------------------------------------------------------
ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#FF2222"

# Your stuff...
# ------------------------------------------------------------------------------
