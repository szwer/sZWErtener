from django.db import models

# Create your models here.
class Url(models.Model):
    short_http = models.SlugField(max_length=10,primary_key=True)
    http = models.URLField(max_length=300)

    def __str__(self):
        return self.http