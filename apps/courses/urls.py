from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'submit$', views.submit, name = "submit"),
    url(r'remove_question$', views.question, name = "question"),
    url(r'remove$', views.remove, name = "remove"),
    url(r'user_courses$', views.user, name = "user_courses"),
    url(r'add_user$', views.add, name = "add_user"),
    url(r'^', views.index, name = "index")
]
