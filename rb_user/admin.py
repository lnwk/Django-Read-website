# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *
# Register your models here.
class OpinionInfoAdmin(admin.ModelAdmin):
    list_display = ['id','oname','oyijian','ophone']

admin.site.register(OpinionInfo, OpinionInfoAdmin)
