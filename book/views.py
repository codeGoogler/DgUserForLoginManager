from django.shortcuts import render
from  django.http import *
from .models import  *
# Create your views here.


def index(request):
    list = Book.objects.all()
    print(list)
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
        "bookInfoList": list,
    }
    return render(request, "learn/index.html", content)