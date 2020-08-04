from selenium import webdriver
import html.parser
import os
import requests

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
def get_linkedin(request):
    
    data = {}
    error = "1"

    try:
        html_source = requests.get(request.POST["url"]).text
        html_source = html_source.split()
        image_checked = False

        for item in html_source:
            item	=	html.parser.HTMLParser().unescape(item)
            if "licdn.com/dms/image" in item and not image_checked:
                img = item.split('content=')[1].split('"/><meta')[0].strip('>').strip('"')
                data['thumbnail'] = img
                image_checked = True


            if "dms.licdn.com" in item:
                url = item.split('"src":')[1].split(',')[0].strip('"')
                data['url'] = url
                error = "0"
                break
    except Exception as e:
        pass

    data['error'] = error
    return Response(data)
            # os.system("wget " + '"' + url + '"')





@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_linkedin2(request):

    test_driver = webdriver.Firefox()
    test_driver.get("https://www.linkedin.com/posts/activity-6688680375654457344-mO_p")

    test_driver.implicitly_wait(2)

    html_source = test_driver.page_source
    html_source = html_source.split()

    for item in html_source:
        item	=	html.parser.HTMLParser().unescape(item)
        if "dms.licdn.com" in item:
            url = item.split('"src":')[1][1:1]
            os.system("wget " + '"' + url + '"')
