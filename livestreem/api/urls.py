from __future__ import absolute_import, print_function, unicode_literals

# from . import routers
from livestreem.api import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from livestreem.views import download

urlpatterns = [
    
    url('trt/1.m3u8', views.get_youtube_link),
    url('trt/2.m3u8', views.youtube_stream),
    url('trt/3.m3u8', views.youtube_stream3),
    
]

urlpatterns += format_suffix_patterns(urlpatterns)