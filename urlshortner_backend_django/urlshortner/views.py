from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import URLModel
import short_url


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
    # ==== getting data ====
    if request.method == "POST":
        data = request.POST
    elif request.data:
        data = request.data
    else:
        return JsonResponse({}, status=400)
    
    # ==== clean the data ====
    if not data.longurl:
        return JsonResponse({'message': 'No field can be empty!'}, status=400)
    elif not isinstance(data.longurl, str): #checks if url sent is unicode
        return JsonResponse({'message': 'URL must be unicode characters!'}, status=400)
    elif len(data.longurl) > 10000:
        return JsonResponse({'message': 'Really?'}, status=400)

    # ==== create the short url ====
    domain = 'heroku.mini.app'
    short_URL = "http://{}/{}".format(domain, short_url.encode_url(data.longurl))
    URL_object = URLModel.objects.create(longurl=data.longurl, shorturl=short_URL)
    return JsonResponse(URL_object, status=201)


