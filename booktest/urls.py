# from django.conf.urls import url
from django.urls import path
from booktest import views as  booktext_view

pathpattern = [
    path('www/',booktext_view.index)
    # path(r'^$',booktext_view.index)
]