from django.contrib import admin
from .models import *


class HeroAdmin(admin.StackedInline):
    extra = 2
    model = Hero


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', "btitle", "bpub_date"]
    list_per_page = 10
    list_filter = ["btitle"]
    search_fields = ["btitle"]
    fieldsets = [
        ("basic", {'fields': ['btitle']}),
        ("more", {'fields': ['bpub_date']}),
    ]
    inlines = HeroAdmin
    inlines = [HeroAdmin]


admin.site.register(Book, BookAdmin)
admin.site.register(Hero)
