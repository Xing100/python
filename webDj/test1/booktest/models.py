from django.db import models


# Create your models here.


#一类
class BookInfo(models.Model):

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    # def __str__(self):
    #     # 返回书名
    #     return self.btitle


#多类
class HeroInfo(models.Model):

    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=False)

    hcomment = models.CharField(max_length=20)

    hbook = models.ForeignKey(BookInfo)

    # def __str__(self):
    #
    #     return self.hname
