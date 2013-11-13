from django.conf.urls import patterns, include, url
from views import documentation
from .decorators import api_doc_protected

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', api_doc_protected(documentation), name='api-documentation'),
)
