from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def info(request):
    return render(request, 'infopage/index.html')


