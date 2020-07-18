
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import json
from django.conf import settings
from zeep.wsse.username import UsernameToken
from zeep import Client
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from lxml import etree
from requests import Session
import uuid
import traceback
import datetime
import youtube_dl
from urllib.request import urlopen
from urllib.parse import unquote
from pytube import YouTube
from pytube import Playlist


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def download_youtube(request):

    url = request.POST.get('url') 
    video = ''
    data= {}
    data['error'] = "1"
    name = ''

    try:
        if url:
            video = YouTube(url)
            name = 'video1'
            # video.streams.get_by_itag(18).default_filename
            video.streams.filter(file_extension = "mp4").all()
            video.streams.get_by_itag(18).download("static", filename = name)
            data['name'] = name + '.mp4'
            data['error'] = "0"

    except Exception as e:
        pass

    return Response(data)







@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def youtube_stream(request):

    ytd =""
    try:
        
        youtube_link = 'https://www.youtube.com/trtarabi/live'
        ytd     =   YouTube(youtube_link)


    except Exception as e:
        print(e)
        pass

    return Response(ytd)




@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def youtube_stream3(request):

    ytd =""
    try:
        

        dataArray = []
        youtube_link = 'https://www.youtube.com/trtarabi/live'
        data = {}
        url_read = ''
        video_url = ''
        ss = ''
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        # youtube_link = request.GET.get('link')
        with ydl:
            result = ydl.extract_info(
                youtube_link,
                download=False # We just want to extract the info
            )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result

        ytd = video['url']

            
        



    except Exception as e:
        print(e)
        pass

    return Response(ytd)





@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_youtube_2(request):

    dataArray = []
    url = request.POST.get('url') 
    # youtube_link = 'https://www.youtube.com/trtarabi/live'
    data = {}
    url_read = ''
    video_url = ''
    error = '1'
    try:
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        # youtube_link = request.GET.get('link')
        with ydl:
            result = ydl.extract_info(
                url,
                download=False, # We just want to extract the info,
                
            )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        # import numpy as np
        # arr = np.array(video['formats'])
        mp4_array = [a for a in video['formats'] if a['acodec'] is not 'none' ]
        # mp4_array = video['formats']
        # newarr = arr[mp4_array]
        thmb_array = [a for a in video['thumbnails'] if a['url'].find('jpg')!=-1  ]
        thumb_url = thmb_array[-1]['url']
        thumb_url = thumb_url[:thumb_url.find('jpg')] + 'jpg'

        # for x in video['formats']:
        #     print(x)

        # data['url'] = mp4_array[0]['url']
        data['name'] = video['title']
        data['error'] = '0'
        data['thumbnail'] = thumb_url
        data['arr'] = mp4_array


    except Exception as e:
        pass

    return Response(data)