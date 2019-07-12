from django.shortcuts import render
from django.http import HttpResponse


def misago_index(request):
    return HttpResponse('misago index')
