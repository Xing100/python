from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    # 图书模型管理类
    list_display = ['id','btitle','bpub_date']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
