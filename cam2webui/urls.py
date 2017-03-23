"""cam2webui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app import views as app_views


urlpatterns = [
    url(r'^$', app_views.index, name='index'),
    url(r'^cameras/$', app_views.cameras, name="cameras"),
    url(r'^settings/$', app_views.settings, name='settings'),
    url(r'^settings/password/$', app_views.password, name='password'),
    url(r'^login/', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
