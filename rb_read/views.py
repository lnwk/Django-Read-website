# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from rb_read.models import readInfo
from rb_books.models import booksInfo
from django.http import JsonResponse
from django.shortcuts import render
# from django.core.paginator import Paginator
# from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator


def read(request, id):

    rchapterList = readInfo.objects.filter(
        books_id=id).order_by('id')
    context = {
        'id': id,
        'rchapterList': rchapterList,


    }
    return render(request, 'rb_read/read.html', context)


def reading(request,id,pageid):

    kneirong = readInfo.objects.filter(books_id=id)

    paginator = Paginator(kneirong, 1)

    kneirong =paginator.page(pageid)


    return render(request, 'rb_read/reading.html', locals())

