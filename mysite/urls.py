from django import views
from django.contrib.sitemaps.views import sitemap
from django.urls import path,include
from website.views import *
from django.conf import settings
from django.conf.urls.static import static
from website.sitemaps import StaticViewSitemap
from django.contrib import admin
from blog.sitemaps import BlogSitemap
import debug_toolbar

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}


urlpatterns = [
    path('admin',admin.site.urls),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('accounts/',include('accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('__debug__/',include(debug_toolbar.urls)),
    path('captcha/', include('captcha.urls')),
]



urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)