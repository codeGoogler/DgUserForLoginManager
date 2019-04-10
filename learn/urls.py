from django.urls import path
from learn import views as i_view


urlpatterns =[
    path('test/',i_view.index),
    path('test2/',i_view.index),

]