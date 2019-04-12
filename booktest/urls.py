# coding:utf-8

from django.urls import path
from django.conf.urls import url
from booktest import views as booktext_view
# from . import *

"""注意，这里一定是urlpatterns，切不可随意用其他的字段"""
urlpatterns = [
    path('wwww/', booktext_view.index),
    path('',booktext_view.index),
    url(r'^(\d+)$',booktext_view.show)
]
