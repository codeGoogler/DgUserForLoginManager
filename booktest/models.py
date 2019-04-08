from django.db import models

# Create your models here.


# Create your models here.
# 报错解答疑问
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        print("title： %s ,日期：%s"%(self.btitle,self.bpub_date))
        return "title： %s ,日期：%s"%(self.btitle,self.bpub_date)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey('BookInfo','on_delete=models.CASCADE()')

    def __str__(self):
        return  self.hname
        # print("title： %s ,日期：%s"%(self.hname,self.hcontent))
        # return 'title： %s ,内容：%s' % (self.hname, self.hcontent)