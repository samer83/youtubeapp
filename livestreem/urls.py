from __future__ import absolute_import, print_function, unicode_literals

# from . import routers
from livestreem.api import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from livestreem.views import download

urlpatterns = [
    
    url('getlink.m3u8', download)

]

urlpatterns += format_suffix_patterns(urlpatterns)