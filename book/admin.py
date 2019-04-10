from django.contrib import admin
from .models import *


# Register your models here.

class HeroAdmin(admin.StackedInline):
    extra = 2
    model = Hero


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', "btitle", "bpub_date"]
    # list_per_page = 10
    # list_filter = ["btitle"]
    # search_fields = ["btitle"]
    # fieldsets = [
    #     ("basic", {'fields': ['btitle']}),
    #     ("more", {'fields': ['bpub_date']}),
    # ]
    # (admin.E103) The value of 'inlines' must be a list or tuple.
    # inlines = HeroAdmin
    inlines = [HeroAdmin]


admin.site.register(Book, BookAdmin)
admin.site.register(Hero)
