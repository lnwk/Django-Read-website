# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from rb_user.islogin import islogin
from models import *
from rb_books.models import booksInfo
from django.http import JsonResponse


@islogin
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid).order_by('-id')

    lenn = len(carts)

    context={'title':'书架',
             'carts':carts,
             'len':lenn}
    return render(request,'rb_cart/cart.html',context)

#添加
@islogin
def add(request,bid):

    uid=request.session['user_id']
    bid = int(bid)

    #查询是否已经有
    carts = CartInfo.objects.filter(user_id=uid, books_id=bid)
    if len(carts) == 0:
        cart = CartInfo()
        cart.user_id = uid
        cart.books_id = bid

    cart.save()




@islogin
def delete(request,cart_id):

    cart = CartInfo.objects.get(pk=int(cart_id))
    cart.delete()

    return render(request, 'rb_cart/cart.html')

