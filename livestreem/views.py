from django.shortcuts import render

# Create your views here.
import requests, os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site




def download(request):
        # file_path = os.path.join(settings.MEDIA_ROOT, path)
        # file_path = path
        # if os.path.exists(file_path):
        #         with open(file_path, 'rb') as fh:
        #                 response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        #                 response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        #                 return response
        
        # from django.contrib.sites.models import Site
        # domain = Site.objects.get_current().domain

        import m3u8
        path = ''.join(['http://', request.get_host(), "/en/api/trt/3.m3u8/"])

        # path =  "{0}/en/api/trt/3.m3u8/".format(request.get_full_path())

        url_read = requests.get(path)
        playlist = m3u8.load(url_read.json())

        # if you want to write a file from its content

        playlist.dump('youtubeapp/static/youtubeapp/playlist.m3u8')

        down = 'youtubeapp/playlist.m3u8'

        file_path = os.path.join(settings.STATIC_ROOT, down)
        if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                        return response

        raise Http404
    

