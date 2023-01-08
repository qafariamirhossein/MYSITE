from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.

def contact_view(request):
    # return HttpResponse('<h1>This is --Home-- page</h1>')
    return render(request,'website/contact.html')

def about_view(request):
    # return HttpResponse('<h1>This is --About-- page</h1>')
    return render(request,'website/about.html')

def index_view(request):
    # return HttpResponse('<h1>This is --About-- page</h1>')
    return render(request,'website/index.html')