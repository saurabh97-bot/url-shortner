from django.db import models

# Create your models here.

from django.db import models

class UrlData(models.Model):
    url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=15)
    def __str__(self):
            return f"Short Url for: {self.url} is {self.short_url}"