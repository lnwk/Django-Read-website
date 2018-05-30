# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from models import *
from hashlib import sha1
from django.http import JsonResponse
from .islogin import islogin
from rb_books.models import booksInfo
from rb_cart.models import *

from django.core.paginator import Paginator


def register(request):
    return render(request,'rb_user/register.html')
def register_handle(requst):
    response = HttpResponse()
    post = requst.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')
    if upwd != ucpwd:
        return redirect('/user/register/')
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    user = UesrInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')



# 判断用户是否已经存在
def register_exist(requset):
    uname = requset.GET.get('uname','')
    count = UesrInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


# 登录界面
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'rb_user/login.html', context)


# 登录处理
def login_handle(request):
    # 接收请求信息
    get = request.POST
    uname = get.get('username')
    upwd = get.get('pwd')
    jizhu = get.get('jizhu', 0)
    # 根据用户名查询对象
    users = UesrInfo.objects.filter(uname=uname)
    # print uname
    # 判断如果未查到则用户名错，查到再判断密码是否正确，
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)

        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/')
            count = CartInfo.objects.filter(user_id=users[0].id).count()

            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname}
            return render(request, 'rb_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname }
        return render(request, 'rb_user/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/user/login')



# 登录用户中心
# 登录用户中心
@islogin
def info(request):
    user_email = UesrInfo.objects.get(id=request.session['user_id']).uemail

    #最近浏览
    books_ids = request.COOKIES.get('books_ids', '')
    books_ids1 = books_ids.split(',')
    books_list=[]

    for books_id in books_ids1:
            books_list.append(booksInfo.objects.get(id=int(books_id)))

    context = {'title': '用户中心',
               'user_email': user_email,
               'user_name': request.session['user_name'],
               'page_name':1,'info':1,
               'books_list':books_list}
    return render(request,'rb_user/user_center_info.html', context)





@islogin
def site(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        oname = request.POST.get('oname')
        oyijian = request.POST.get('oyijian')
        ophone = request.POST.get('ophone')

        opinion = OpinionInfo()
        opinion.user_id = user_id
        opinion.oname = oname
        opinion.oyijian = oyijian
        opinion.ophone = ophone
        opinion.save()

    return render(request, 'rb_user/user_center_site.html')











