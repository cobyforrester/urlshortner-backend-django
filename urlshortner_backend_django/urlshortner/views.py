from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import URLModel
import short_url

def home_page(request, *args, **kwargs):
    
    if request.method == "POST":
        if request.POST.get('LongURl'):
            #Create an object to be saved into the model
            short_URL = URLModel.objects.create(longurl = longURL)
            domain = 'mini'
            longURL = request.POST.get('LongURL')
            
            
            short_URL = request.POST.get('LongURL')
            print(short_URL)

            #Create an object to be saved into the model
            short_URL = URLModel(longurl = longURL, shorturl = None)
            return render(request, 'home.html', context={'urlItem': short_URL}, status=200)
    else:
        return render(request, 'home.html', context={}, status=200)

'''
def Long2Short(request, *args, **kwargs):

    if request.method == "POST":
        print("hi ho")
        short_URL = "done"

    return HttpResponseRedirect("/")
'''