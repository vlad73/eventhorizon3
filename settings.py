try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

import os

# setup default datastore paths
_ds_pathinfo = {
    'datastore_path': '../data/eventhorizon',
    'history_path': '../data/eventhorizon.history',
}

DATABASES['default'].update(_ds_pathinfo)


SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'djangotoolbox',
#    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'gateway',
)

if has_djangoappengine:
    INSTALLED_APPS = ('djangoappengine',) + INSTALLED_APPS

TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'
EKKLI_SERVER_URL = "http://beta.ekkli.com/"