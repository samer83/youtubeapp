from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
from cms.models import CMSPlugin
from django.utils.translation import ugettext, ugettext_lazy as _

@python_2_unicode_compatible
class DownloaderContainer(CMSPlugin):

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=200)

    def __str__(self):
        return self.title