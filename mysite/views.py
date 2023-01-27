from django.http import HttpResponse
from django.contrib import admin

def helloWorld(request):
    return HttpResponse('<h1>Hello World !!! FUCK people</h1>')