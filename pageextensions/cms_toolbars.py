
from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool	import toolbar_pool


from .models import PageExtension


@toolbar_pool.register
class PageExtension_Toolbar(ExtensionToolbar):

	model 		=	PageExtension

	def populate(self):

		current_page_menu		=	self._setup_extension_toolbar()

		if current_page_menu:

			page_extension, url 	=	self.get_page_extension_admin()

			if url:
				current_page_menu.add_break()
				current_page_menu.add_modal_item(
					'Custom Settings',
					url		=	url,
					disabled=not self.toolbar.edit_mode_active,
					)
