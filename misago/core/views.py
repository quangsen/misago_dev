from django.shortcuts import render
from django.http import HttpResponse


def home_redirect():
    return 'vvv'


def forum_index(request):
    return HttpResponse('forum_index')