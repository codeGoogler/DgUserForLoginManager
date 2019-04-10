# coding:utf8
from django.shortcuts import render
from django.http import  *
# Create your views here.


from django.http import *


# def index():
#     ss = "123"
#     reslut = ss.encode('gbk')
#     return HttpResponse(reslut)
#     # return HttpResponse("hello ，world")
#     # return HttpResponse("你咋不还我钱呢，哒哒哒啊".encode("utf-8"))
#     # return HttpResponse("你咋不还我钱呢，哒哒哒啊".encode("utf-8"))
#     # response =requests.get("http://www.qq.com/")
#     # response.encoding="gbk"
# # return  HttpResponse("你咋不还我钱呢，哒哒哒啊".encode("gbk"))

def index(request):
    # i = input("请输入i：")
    # j = input("请输入j：")
    # ss = int(i) * input(j)
    ss = 100
    return HttpResponse(("你咋不还我钱呢，哒哒哒啊"%ss).encode("utf-8"))
