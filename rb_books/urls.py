#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
import views


urlpatterns=[
      url(r'^$',views.index),
      url(r'^list(\d+)_(\d+)_(\d+)/$', views.booklist),
      url(r'^(\d+)/$', views.detail),
      url(r'^newsbooks/$', views.newsbooks),
      url(r'^hotlists/(\d+)$',views.hotlists),
]