

from __future__ import unicode_literals
from django.db import models

class UesrInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemail=models.CharField(max_length=30)
    uzipcode = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')
    utitle = models.CharField(max_length=20, default='')
    ucontent=models.CharField(max_length=100,default='')


class OpinionInfo(models.Model):
    user = models.ForeignKey('rb_user.UesrInfo')
    oname=models.CharField(max_length=20)
    oyijian=models.CharField(max_length=200)
    ophone=models.CharField(max_length=11,default='')
    def __str__(self):
        return self.ttitle.encode('utf-8')





