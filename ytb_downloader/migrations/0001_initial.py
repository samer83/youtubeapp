# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-16 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='livestreemContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ytb_downloader_livestreemcontainer', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
