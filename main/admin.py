from django.contrib import admin
from .models import Url
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('short_http', 'http')

admin.site.register(Url, UrlAdmin)