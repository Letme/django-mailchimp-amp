#_*_coding: utf-8_*_

from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.mailchimp_proxy_view),
]
