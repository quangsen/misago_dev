from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


def index_runtest(request):
    words = ['Welcome', 'to', 'my', 'site.']
    output = _(' '.join(words))
    return HttpResponse(output)
