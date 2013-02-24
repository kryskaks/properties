from django.conf.urls.defaults import patterns, include, url
from listing.views import index, init, delete, detail

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^properties/$', index),
	url(r'^properties/init/$', init),
	url(r'^properties/delete/$', delete),
	url(r'^properties/(?P<property_id>\d+)/$', detail),
) 