# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
import requests
from django.http import HttpResponse, HttpResponseRedirect, Http404

from . import models

import os
from django.conf import settings

class mTextPlugin(CMSPluginBase):
    model = models.m_text_model
    name = 'm_Text'
    render_template = 'm_text/model.html'
    allow_children = False


    def render(self, context, instance, placeholder):

      
        context.update({
                'instance': instance,
                'placeholder': placeholder,
        })

        return context 


plugin_pool.register_plugin(mTextPlugin)
