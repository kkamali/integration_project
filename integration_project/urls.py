"""integration_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.integrate.urls', namespace = "integrate")),
    url(r'disappearing_ninjas_assignment/', include('apps.disappearingninjas.urls', namespace = "disappearingninjas")),
    url(r'ninja_gold_assignment/', include('apps.ninjagold.urls', namespace = "ninjagold")),
    url(r'random_word_assignment/', include('apps.randomword.urls', namespace = "randomword")),
    url(r'courses/', include('apps.courses.urls', namespace = "courses")),
    url(r'loginregister/', include('apps.loginregister.urls', namespace = "login_register"))
]
