from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import URLModel
from django.conf import settings
import short_url

DOMAIN_NAME = settings.DOMAIN_NAME
def home_page(request, *args, **kwargs):
    URL_object = None
    if request.method == "POST":
        if request.POST.get('LongURL'):
            #Get the user's long URL
            longURL = request.POST.get('LongURL')
            #Create an object to be saved into the model
            URL_object = URLModel.objects.create(longurl = longURL)
            #Create a short url
            domain = 'mini'
            id = URL_object.id
            short_URL = "http://{}/{}".format(domain, short_url.encode_url(id))
            print(short_URL)
            URL_object_return = URLModel.objects.get(id=id)
            URL_object_return.shorturl = short_URL
            URL_object_return.save()
        return render(request, 'home.html', context={'urlItem': URL_object_return.shorturl}, status=200)
    else:
        return render(request, 'home.html', context={}, status=200)

'''
def Long2Short(request, *args, **kwargs):

    if request.method == "POST":
        print("hi ho")
        short_URL = "done"

    return HttpResponseRedirect("/")
'''

def api_shorturl_processor(request,*args, **kwargs):
    '''
    API endpoint 
    Consume with vue.js
    return Json
    '''

    # ==== request type ====
    if not request.method == "POST":
        return JsonResponse({'message': 'Must be post!'}, status=400)

    # ==== getting data ====
    if request.POST:
        longurl = request.POST.get('LongURL')
    elif request.data:
        longurl = request.data['LongURL']
    else:
        return JsonResponse({}, status=400)
    
    print(longurl)
    # ==== clean the data ====
    if not longurl:
        return JsonResponse({'message': 'No field can be empty!'}, status=400)
    elif not isinstance(longurl, str): #checks if url sent is unicode
        return JsonResponse({'message': 'URL must be unicode characters!'}, status=400)
    elif len(longurl) > 10000:
        return JsonResponse({'message': 'Really?'}, status=400)

    # ==== if already in DB ==== 
    qs = URLModel.objects.filter(longurl=longurl)
    if qs.exists():
        obj = qs.first()
        return JsonResponse({'shorturl': obj.shorturl}, status=200)

    # ==== create the short url ====
    id = URLModel.objects.all().count()
    short_URL = "http://{}/{}".format(DOMAIN_NAME, short_url.encode_url(id))
    URL_object = URLModel.objects.create(longurl=longurl, shorturl=short_URL)
    return JsonResponse({'shorturl': short_URL}, status=201)


