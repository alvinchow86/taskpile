from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
 
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'tasks/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),                   
    (r'^', include('taskmaster.taskpile.urls')),
                     
)
