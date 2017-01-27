"""URLshortenerSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from URLshortenerApp.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login),
    url(r'^home/$', home, name='home'),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^URLShortner/$', shorten_url, name='shortenurl'),
    url(r'^delete/$', deleteRec, name='delete'),
    url(r'^logout/$', logout_page),
    # when short URL is requested it redirects to original URL
    url(r'^(?P<short_id>\w+)/$', redirect_original , name='redirectoriginal'),

               
               

]
