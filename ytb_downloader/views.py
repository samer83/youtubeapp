from django.shortcuts import render
from .download_file import download
# Create your views here.
from django.utils.translation import get_language
from django.shortcuts import render, redirect

def vdownload(request): #update the cart
    # print(request.POST)
    try:
        # request = context['request']
        url = request.POST.get('inputurl')

        
        download(url)
        return redirect("d Müzikleri - Saz-ı Aşık v2(Sonu Farklı) By Yıldıray GÜRGEN.mp4".format(get_language()))

        # CartPlugin.render(request, cart, "content")
        

                # cart.pages_extensions.add(page_extension)
    except Exception as e:
        print (e)


	# return redirect(page_obj.get_absolute_url()) # go to that page after add it
	# return redirect("/{0}/cart/".format(get_language()))
	# return redirect("cart:home")


