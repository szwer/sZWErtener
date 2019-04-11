from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^(?P<short_http>\w{10})$', views.original, name='original'),

    url(r'^makeshort/$', views.shorten, name='shorten'),
]