from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from .models import Url
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('main/index.html', c)


def original(request, short_http):
    url = get_object_or_404(Url, pk=short_http)
    url.save()
    return HttpResponseRedirect(url.http)


def shorten(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_http = get_short_code()
        b = Url(http=url, short_http=short_http)
        b.save()

        response_data = {}
        response_data['url'] = "Twój nowy URL: " + settings.SITE_URL + "/" + short_http
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")


def get_short_code():
    length = 10
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase

    while True:
        short_http = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Url.objects.get(pk=short_http)
        except:
            return short_http