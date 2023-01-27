from django import views
from django.urls import path,include
from website.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin',admin.site.urls),
    # path('about',about_view),
    # path('home',home_view),
    # path('contact',contact_view),
    path('',include('website.urls')),
    path('blog/',include('blog.urls'))
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)