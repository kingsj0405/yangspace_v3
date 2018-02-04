"""YangSpace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

import blog.views as blog_views

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),
    # account
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    # blog
    url(r'^blog/page/create/$', blog_views.create, name='create'),
    url(r'^blog/page/create/(?P<parent_url>[\w\-]+)/$', blog_views.create, name='create'),
    url(r'^blog/page/read/$', blog_views.read, name='read'),
    url(r'^blog/page/read/(?P<page_url>[\w\-]+)/$', blog_views.read, name='read'),
    url(r'^blog/page/update/$', blog_views.update, name='update'),
    url(r'^blog/page/update/(?P<page_url>[\w\-]+)/$', blog_views.update, name='update'),
    url(r'^blog/page/delete/$', blog_views.delete, name='delete'),
    url(r'^blog/page/delete/(?P<page_url>[\w\-]+)/$', blog_views.delete, name='delete'),
    url(r'^blog/download/debug_info/$', blog_views.download_debug_info, name='download-debug-info'),
    url(r'^blog/', blog_views.main, name='main'),
    url(r'^', blog_views.index, name='index'),
]
