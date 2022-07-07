from django.contrib import admin
from booktest.models import BookInfo
from booktest.models import HeroInfo

# Register your models here.


admin.site.register(BookInfo)
admin.site.register(HeroInfo)
