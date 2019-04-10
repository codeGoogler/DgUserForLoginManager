from django.shortcuts import render
from django.http import *


# Create your views here.

def index(request):
    # ss = 100
    # return HttpResponse("你好啊，卡卡罗特 %d lallal"%ss)
    # return HttpResponse(("你好啊，卡卡罗特 %d"%ss).encode("utf8"))
    # temp = loader.get_template("learn/index.html")
    # return  HttpResponse(temp.render())
    return render(request, "learn/index.html")
