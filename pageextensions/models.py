from django.db import models
# from django.contrib.auth.models import User
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.conf import settings
from filer.fields.image import FilerImageField
from ckeditor_uploader.fields import RichTextUploadingField

User        =   settings.AUTH_USER_MODEL

class PageExtension(PageExtension):
	subtitle	=	models.CharField(blank=True, max_length=200)
	# description	=	models.TextField(blank=True)
	description = RichTextUploadingField()


	background	=	FilerImageField(null=True, blank=True)
	author = models.ForeignKey(
			User,
			related_name='author',
			unique=False, null=True, blank=True
		)

extension_pool.register(PageExtension)