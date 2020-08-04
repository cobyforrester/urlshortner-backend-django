"""urlshortner_backend_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from urlshortner.views import home_page, api_shorturl_processor, shortURL_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    #path('processing/', Long2Short),
    path('api/urlshortner/process', api_shorturl_processor),
    re_path(r'^((?!\/admin).)*$', shortURL_redirect),
    
]
