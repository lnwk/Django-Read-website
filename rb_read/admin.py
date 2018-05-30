# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *
# Register your models here.

class readInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['id','rchapter','rneirong','zj_id']

admin.site.register(readInfo,readInfoAdmin)