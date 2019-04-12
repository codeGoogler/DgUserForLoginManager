from django.urls import path
from book import views as book_view

urlpatterns = [
    path('book/', book_view.index)
]
