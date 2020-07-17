
import requests
import os
from django.conf import settings
# from .middleware import ForceResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404

from pytube import YouTube

# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt
#%matplotlib inline
# image operation
import cv2



def download(url):

    video = YouTube(url)
    video.streams.filter(file_extension = "mp4").all()
    video.streams.get_by_itag(18).download()

    

