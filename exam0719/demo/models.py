from django.db import models

# Create your models here.
class bookinfo(models.Model):
    bookname = models.CharField(max_length=20)  #图书名称
    book_gender = models.CharField(max_length=20)   #图书种类
    book_id = models.CharField(max_length=20)   #图书编号
    bcontent = models.CharField(max_length=20)  #图书内容
