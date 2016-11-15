from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'ninjas/(?P<ninja>[A-Za-z]*)$', views.ninja, name = "ninja")
]
