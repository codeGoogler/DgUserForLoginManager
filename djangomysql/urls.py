from django.conf.urls import url
from django.urls import path
from djangomysql import views as django_view



urlpatterns =[
    url(r'^$',django_view.index),
]