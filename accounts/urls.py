from django.conf.urls import url 
from django.contrib.auth.views import login
from accounts import views

urlpatterns = [
	url(r'^signup/$', views.signup),
	url(r'^login/$', login),
	url(r'^profile/$', views.profile),
]