# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models
from rb_books.models import booksInfo

# Create your models here.
class readInfo(models.Model):
    books = models.ForeignKey('rb_books.booksInfo')
    rchapter = models.CharField(max_length=200)
    rneirong = HTMLField()
    zj_id = models.IntegerField()


    def __str__(self):
        return self.rchapter.encode('utf-8')

