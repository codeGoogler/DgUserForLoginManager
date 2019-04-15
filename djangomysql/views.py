from django.shortcuts import render
from django.http import *
from djangomysql.models import *
# Create your views here.


def index(request):
    bookInfo = BookInfo.bookManager2.all()
    content = {
        'bookList':bookInfo.values()
    }
    return render(request,"djangomysql/index.html",content)