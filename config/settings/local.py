from .base import *

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='FNKner4lgCcCYlO9VSPRVqvdOTDcQVKm7U0gulT6iEHz2rQjZd6VM3Kydkib1gPM')
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

# Celery
# ------------------------------------------------------------------------------
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-always-eager
CELERY_TASK_ALWAYS_EAGER = True
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True

CELERY_BEAT_SCHEDULE['test-task1'] = {
    'task': 'deleteme.test_app.tasks.task1',
    'schedule': 10,
}

CELERY_BEAT_SCHEDULE['test-task2'] = {
    'task': 'deleteme.test_app.tasks.task2',
    'schedule': 60,
}

# django_admin_env_notice
# ------------------------------------------------------------------------------
ENVIRONMENT_NAME = "Development"
ENVIRONMENT_COLOR = "#8E8E8E"

# TEST APP
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['deleteme.test_app']

# Your stuff...
# ------------------------------------------------------------------------------
