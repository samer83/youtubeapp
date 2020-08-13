from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from .models import PageExtension

class PageExtension_Admin(PageExtensionAdmin):
	pass

admin.site.register(PageExtension, PageExtension_Admin)