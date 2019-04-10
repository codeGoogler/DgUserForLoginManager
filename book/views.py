from django.shortcuts import render
from  django.http import *
# Create your views here.


def index(request):
    return HttpResponse("卡卡罗特，你好啊".encode("utf-8"))