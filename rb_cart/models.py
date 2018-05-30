# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey('rb_user.UesrInfo')
    books = models.ForeignKey('rb_books.booksInfo')
    count = models.IntegerField(default=0)



