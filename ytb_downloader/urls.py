from django.conf.urls import url

from .views import (
        vdownload,
        )

urlpatterns = [
    # url(r'^$', View., name='home'),
    url(r'^download', vdownload, name='vdownload', ),
]



