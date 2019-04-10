from django.urls import path
from learn import views as i_view
from django.conf.urls import url



urlpatterns =[
    # 什么都不写
    url(r'^$',i_view.index)
]