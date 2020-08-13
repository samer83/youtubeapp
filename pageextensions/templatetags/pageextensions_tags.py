from cms.models import Title, Page
from django.template import Library, Node

register = Library()

@register.filter
def get_page_background(name):
	value = ""
	try:
		# thisPage = Page.objects.get(id=id)
		pageID 	= Title.objects.filter(slug=name, publisher_is_draft=True).values('page_id')
		thisPage = Page.objects.get(id=pageID)
		if thisPage:
			value = thisPage.pagefieldextension.background.url
			# Title.objects.filter(page_id__in[var]).values('title')
			# page = Title.objects.filter(slug="packages”)
	except :
		pass
	return value

@register.filter
def get_page_author(name):
	value = ""
	try:
		# thisPage = Page.objects.get(id=id)
		pageID 	= Title.objects.filter(slug=name, publisher_is_draft=True).values('page_id')
		thisPage = Page.objects.get(id=pageID)
		if thisPage:
			value = thisPage.pagefieldextension.background.url
			# Title.objects.filter(page_id__in[var]).values('title')
			# page = Title.objects.filter(slug="packages”)
	except :
		pass
	return value


@register.simple_tag
def get_pageDescription(name):
	value = ""
	try:
		# thisPage = Page.objects.get(id=id)
		pageID 	= Title.objects.filter(slug=name, publisher_is_draft=True).values('page_id')
		thisPage = Page.objects.get(id=pageID)
		if thisPage:
			value = thisPage.pagefieldextension.description
	except :
		pass
	return value



@register.simple_tag
def get_pageLink(name):
	value = ""
	try:
		# thisPage = Page.objects.get(id=id)
		pageID 	= Title.objects.filter(slug=name, publisher_is_draft=True).values('page_id')
		thisPage = Page.objects.get(id=pageID)
		if thisPage:
			value = thisPage.get_absolute_url()
	except :
		pass
	return value




# 	@register.simple_tag
# def get_pageUrl(name):
# 	url = ""
# 	try:
# 		# thisPage = Page.objects.get(id=id)
# 		thisPage 	= Title.objects.filter(slug=name)
# 		if thisPage:
# 			url = thisPage.pagefieldextension.description
# 	except :
# 		pass
# 	return url

