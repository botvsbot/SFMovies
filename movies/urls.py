from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'about/', views.about, name='about'),
	url(r'da/', views.da, name='da'),
	url(r'data/', views.data, name='data'))
