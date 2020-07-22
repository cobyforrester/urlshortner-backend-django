from django.shortcuts import render
from .models import URLModel

def basic_view(request, *args, **kwargs):
    qs = URLModel.objects.all()
    url = qs.first()
    print(url.longurl)
    return render(request, 'home.html', context={'urlItem':url}, status=200)
