from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    url(r'^$', 'zkwiki.wiki.views.home', name='wiki-home'),
)
