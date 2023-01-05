from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about',about_view),
    path('home',home_view),
    path('contact',contact_view)
]
