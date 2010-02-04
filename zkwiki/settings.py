import os

ROOT_URLCONF = 'zkwiki.urls'

# XXX: http://code.djangoproject.com/ticket/12428
DATABASE_ENGINE = 'dummy'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'zkwiki.wiki',
)

ROOT_PATH = os.path.dirname(__file__).replace('\\', '/')
TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

try:
    from settings_local import *
except ImportError:
    pass
