from django.contrib import admin
from .models import *


# Register your models here.


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 4



# 自定义页面管理
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    # 分页加载
    list_per_page = 10
    # 添加、修改页属性

    # 属性的先后顺序
    # fields = ['btitle', 'bpub_date']
    # 属性分组
    fieldsets = [
        ("basic", {'fields': ['btitle']}),
        ("more", {'fields': ['bpub_date']}),
    ]
    inlines = [HeroInfoInline]



# 向admin注册booktest模型

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
