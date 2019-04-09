# coding=utf-8
from django.shortcuts import render

# Create your views here.


from django.http import *


def index():
    # ss = "123"
    # reslut = ss.encode('utf8')
    # return HttpResponse(reslut)
    # return HttpResponse("hello ，world")
    return HttpResponse("你咋不还我钱呢，哒哒哒啊".encode("gbk"))
    # return HttpResponse("你咋不还我钱呢，哒哒哒啊".encode("utf-8"))
    # response =requests.get("http://www.qq.com/")
    # response.encoding="gbk"
# return  HttpResponse("你咋不还我钱呢，哒哒哒啊".encode("gbk"))
