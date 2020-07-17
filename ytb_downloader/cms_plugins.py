# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
import requests
# from .middleware import ForceResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404

from . import models
# from .record import record_stream

import os
from django.conf import settings

class DownloaderPlugin(CMSPluginBase):
    model = models.DownloaderContainer
    name = 'youtube downloader'
    render_template = 'ytb_downloader/model.html'
    allow_children = False


    def render(self, context, instance, placeholder):

        print('i am inn')

        # url = "https://www.youtube.com/trtarabi/live"
        # record_stream(url,"youtubeapp/static/youtubeapp/11",10)


        # url = "http://localhost:8080/en/api/trt/3.m3u8/"

        

        # import urllib.request 
        # with urllib.request.urlopen('http://127.0.0.1:8080/static/youtubeapp/playlist.m3u8') as f:
        #         html = f.read().decode('utf-8')
        # import urllib.request
        # urllib.request.urlretrieve ("http://127.0.0.1:8080/static/youtubeapp/playlist.m3u8", "mp3.mp3")

        # raise ForceResponse(HttpResponseRedirect("{0}".format(down), context))









        # with open("playlist.m3u8", "rb") as in_file, open("playlist11.m3u8", "wb") as out_file:
        #         out_file.write(in_file.read())

        # open('playlist2.m3u8', 'wb').write(open("playlist.m3u8", "rb") )


        # open("playlist.m3u8", "rb") 

        # print('start your stream here')
        # request = context['request']
        # url = "http://localhost:8000/en/api/trt/1.m3u8/"
        # # from urllib.request import urlopen  
        # # url_read = urlopen(url).read()

        # url_read = requests.get(url)
        # url_json = url_read.json()
        # file = open("youtubeapp/static/youtubeapp/11.m3u8", "w") 
        # file.write(url_json) 
        # file.close() 

        # # urlopen(file).read()

        
        context.update({
                'instance': instance,
                'placeholder': placeholder,
                # 'pages_extensions': pages_extensions
        })

        return context 


plugin_pool.register_plugin(DownloaderPlugin)
