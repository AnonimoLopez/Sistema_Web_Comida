from django.conf.urls import url
from apps.usuarios.views import *
urlpatterns = [
    url(r'^welcome',  inicio),
]
