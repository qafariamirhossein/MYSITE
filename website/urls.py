from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name ='website'

urlpatterns = [
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('',index_view,name='index'),
    path('test',test_view,name='test'),
    path('newsletter',newsletter_view,name='newsletter')
]
