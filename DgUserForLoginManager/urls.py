"""DgUserForLoginManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from booktest import views as learn_views
from book import views as  book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('goBook/', views.index),
    path('www/', learn_views.index),
    path('test/', book_view.index),
    url(r'^',include("learn.urls")),
    url(r'^learn/',include("learn.tinyma_urls")),
    url(r'^',include("learn.tinyma_urls")),
    url(r'^',include("learn.tinymy_urls")),
]
