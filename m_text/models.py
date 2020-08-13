from django.db import models
from django.contrib.auth.models import User
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.utils.encoding import python_2_unicode_compatible
from cms.models import CMSPlugin
from django.utils.translation import ugettext, ugettext_lazy as _
from filer.fields.image import FilerImageField
from ckeditor_uploader.fields import RichTextUploadingField


@python_2_unicode_compatible
class m_text_model(CMSPlugin):
    body = RichTextUploadingField()
    
    def __str__(self):
        return str(self.id)
