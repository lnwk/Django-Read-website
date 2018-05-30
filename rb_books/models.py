#  coding: utf-8
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
#书分类
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

class booksInfo(models.Model):
    btitle = models.CharField(max_length=50)
    bpic = models.ImageField(upload_to='rb_books')
    isDelete = models.BooleanField(default=False)
    bclick = models.IntegerField()
    bjianjie = models.CharField(max_length=200)
    bcontent = HTMLField()
    btype = models.ForeignKey(TypeInfo)

    def __str__(self):
        return self.btitle.encode('utf-8')


