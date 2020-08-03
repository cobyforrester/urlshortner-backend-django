from django.db import models

class URLModel(models.Model):
    longurl = models.TextField(null=False, blank=False)
    shorturl = models.CharField(max_length=7)
