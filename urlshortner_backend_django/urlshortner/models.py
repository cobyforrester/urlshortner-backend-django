from django.db import models

class URLModel(models.Model):
    longurl = models.CharField(max_length=100)
    shorturl = models.CharField(max_length=7)
