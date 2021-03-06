from django.conf.urls import patterns, url
from apps.myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^habit/(?P<id_hash>[a-z0-9]+)$', views.detail, name='detail'),
    url(r'^latest/$', views.latest, name='latest'),
)