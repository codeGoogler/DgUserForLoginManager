# coding:utf8
from django.shortcuts import render
from django.http import *
# Create your views here.
from booktest.models import BookInfo
from .models import *

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
    # ss = 100
    # return HttpResponse(("你咋不还我钱呢，哒哒哒啊%d"%ss).encode("utf8"))

    list1 = BookInfo.objects.all()
    print(list1)
    content = {
        "t1": "张三",
        "t2": "李四",
        "t3": "王五",
        "t4": "赵六",
        "t5": "贝吉塔",
        "t6": "卡卡罗特",
        "t7": "亚奇洛贝",
        "t8": "天津饭",
        "t9": "龟仙人",
        "bookInfoList": list1,
    }
    return render(request, "learn/index.html", content)


def show(request,index):
    book = BookInfo.objects.get(pk=index)
    print(book)
    # 从书中去找英雄ing
    heroList = book.heroinfo_set.all()
    content = {
        "list":heroList
    }
    if heroList == None:
        print("======================================================")
    print(heroList)
    return render(request, "booktest/show.html", content)
