"""tjif URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from web import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^add-jam$', views.add_jam, name='add_jam'),
    url('^profile/(?P<username>.*)/$', views.profile, name='profile'), 
    url('^profile/$', views.profile, name='profile'),
    url('^jam/(?P<jam_id>.*)/$', views.jam, name='jam'),    
    url('^follow/(?P<username>.*)/$', views.follow, name='follow'),
    url('^discover$', views.discover, name='discover'),
    url('^login$', views.login, name='login'),    
]
