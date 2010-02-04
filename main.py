import logging
import os
import sys

from google.appengine.ext.webapp import util

# Remove the standard version of Django.
for k in [k for k in sys.modules if k.startswith('django')]:
    del sys.modules[k]

# Set up the environment so that the local Django can be imported.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'zkwiki.settings'

import django.core.handlers.wsgi
import django.core.signals
import django.db

# Log errors.
def log_exception(*args, **kwds):
    logging.exception('Exception in request:')
django.core.signals.got_request_exception.connect(log_exception)

# Unregister the rollback event handler.
django.core.signals.got_request_exception.disconnect(
    django.db._rollback_on_exception,
)

def main():
    application = django.core.handlers.wsgi.WSGIHandler()
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
