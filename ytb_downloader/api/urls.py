from __future__ import absolute_import, print_function, unicode_literals

# from . import routers
from ytb_downloader.api import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url('youtube/', views.download_youtube),
    
]

urlpatterns += format_suffix_patterns(urlpatterns)