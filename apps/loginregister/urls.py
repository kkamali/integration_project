from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register$', views.register, name = "register"),
    url(r'login$', views.login, name = "login"),
    url(r'go_back$', views.go_back, name = "go_back"),
    url(r'^', views.index, name = "index"),
]
