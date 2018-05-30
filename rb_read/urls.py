from django.conf.urls import url
import views

urlpatterns = [
      url(r'^(\d+)/$', views.read),
      url(r'^(\d+)/page=(\d+)/$', views.reading),
]