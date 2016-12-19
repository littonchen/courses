from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^course/destroy/(?P<id>\d+)$', views.removecourse),
	url(r'^delete/(?P<id>\d+)$', views.deletecourse),
	url(r'^createcourse$', views.createcourse),
	url(r'^$', views.index),
]