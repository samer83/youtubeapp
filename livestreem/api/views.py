
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
def get_youtube_link(request):

    ss ='''#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:2
#EXT-X-MEDIA-SEQUENCE:82463
#EXT-X-DISCONTINUITY-SEQUENCE:2
#EXT-X-PROGRAM-DATE-TIME:2020-06-09T14:29:10.617+00:00
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82463/goap/clen%3D44425%3Blmt%3D1591548017620113/govp/clen%3D788540%3Blmt%3D1591548017620118/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82464/goap/clen%3D44607%3Blmt%3D1591548017620127/govp/clen%3D775028%3Blmt%3D1591548017620130/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82465/goap/clen%3D44678%3Blmt%3D1591548017620141/govp/clen%3D707429%3Blmt%3D1591548017620142/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82466/goap/clen%3D44925%3Blmt%3D1591548017620155/govp/clen%3D718340%3Blmt%3D1591548017620161/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82467/goap/clen%3D44405%3Blmt%3D1591548017620169/govp/clen%3D694281%3Blmt%3D1591548017620174/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82468/goap/clen%3D44309%3Blmt%3D1591548017620183/govp/clen%3D722377%3Blmt%3D1591548017620194/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82469/goap/clen%3D44930%3Blmt%3D1591548017620197/govp/clen%3D601083%3Blmt%3D1591548017620209/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82470/goap/clen%3D44907%3Blmt%3D1591548017620211/govp/clen%3D589571%3Blmt%3D1591548017620216/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82471/goap/clen%3D44140%3Blmt%3D1591548017620225/govp/clen%3D569950%3Blmt%3D1591548017620230/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82472/goap/clen%3D44656%3Blmt%3D1591548017620239/govp/clen%3D580370%3Blmt%3D1591548017620244/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82473/goap/clen%3D44478%3Blmt%3D1591548017620253/govp/clen%3D642935%3Blmt%3D1591548017620258/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82474/goap/clen%3D45068%3Blmt%3D1591548017620267/govp/clen%3D630246%3Blmt%3D1591548017620273/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82475/goap/clen%3D44091%3Blmt%3D1591548017620281/govp/clen%3D653814%3Blmt%3D1591548017620292/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82476/goap/clen%3D44845%3Blmt%3D1591548017620295/govp/clen%3D572017%3Blmt%3D1591548017620305/dur/2.000/file/seg.ts
#EXTINF:2.0,
https://r7---sn-8p85-3fpr.googlevideo.com/videoplayback/id/mnobQe-PZKk.0/itag/95/source/yt_live_broadcast/expire/1591734534/ei/ppzfXvORHrmrxN8P-JC6uAI/ip/94.129.86.124/requiressl/yes/ratebypass/yes/live/1/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r7---sn-8p85-3fpr.googlevideo.com/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/3810/mh/Le/mm/44/mn/sn-8p85-3fpr/ms/lva/mv/m/mvi/6/pl/22/keepalive/yes/mt/1591712785/disable_polymer/true/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,goi,sgoap,sgovp,playlist_duration,manifest_duration,vprv,playlist_type/sig/AOq0QJ8wRQIgZztovmTtaIfVH4oozMs-a-xNaZQad4iUNiDsWwrHyYECIQCw_V8cYOQ9Dxoa585xoOLJEBROQKLoelC3_2eHQU6uWA%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/AG3C_xAwRQIhAI37TZosWbuQ1Q9Tvj7PHYQgAqy7o-Ovmt0wn1Vv3YrWAiBGHKBJT7AWx5Ithg-rDzG_dqcRhS6l040qH90oGJC4Gg%3D%3D/playlist/index.m3u8/sq/82477/goap/clen%3D44831%3Blmt%3D1591548017620309/govp/clen%3D621455%3Blmt%3D1591548017620315/dur/2.000/file/seg.ts
'''
    # from django.core.files import File
    # f = open('/index.m3u8', 'r')
    # myfile = File(f)

    # return Response(myfile)
    # return Response(ss)

    dataArray = []
    youtube_link = 'https://www.youtube.com/trtarabi/live'
    data = {}
    url_read = ''
    video_url = ''
    ss = ''
    try:
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

        print("******************************************")
        print(video['url'])
        video_url = video['url']
        return Response(video_url)
        print("******************************************")

        # response = urllib2.urlopen(video_url)
        # print(response)
        # f = response.read()
        #print('i am here')
        url_read = urlopen(video_url).read()
        print('*******************url_read****************')
        print(url_read)
        # ss = url_read.replace('\n', '\r\n')
        ss = str(url_read.decode("utf-8") )

        

        print('*******sssssssssssssss')
        print(ss)
        # print(unquote(str(url_read)))

        # f = open(video_url, "r")
        # print(f)

        
        # data['url'] = video_url

        # json_data = json.dumps(data)
        # dataArray.append(json.loads(json_data))

    except Exception:
        pass

    return Response(ss)







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




