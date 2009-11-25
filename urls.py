from django.conf.urls.defaults import *
from django.contrib import admin
from seivanheidari import settings
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^admin/', include(admin.site.urls)),
    (r'^seivanheidari_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^blog/', include('seivanheidari.blog.urls')),
    (r'^', include('seivanheidari.blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    #(r'^', include('seivanheidari.flatpage_extended.urls'))
    
)
