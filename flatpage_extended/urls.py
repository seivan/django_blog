from django.conf.urls.defaults import *

urlpatterns = patterns('seivanheidari.flatpage_extended.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
