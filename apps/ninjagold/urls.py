from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^submit_gold/(?P<location>[a-z]*)$', views.gold, name = "gold")
]
