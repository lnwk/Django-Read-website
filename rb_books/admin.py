# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
class booksInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'btitle',  'bcontent', 'btype']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(booksInfo,booksInfoAdmin)