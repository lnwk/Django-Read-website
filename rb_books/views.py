# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import booksInfo,TypeInfo
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
# 查询每类书籍最新的4个和点击率最高的4个
def index(request):

    count = request.session.get('count')
    lishi = booksInfo.objects.filter(btype__id=1).order_by("-id")[:4]
    lishi2 = booksInfo.objects.filter(btype__id=1).order_by("-bclick")[:4]
    wuxia = booksInfo.objects.filter(btype__id=2).order_by("-id")[:4]
    wuxia2 = booksInfo.objects.filter(btype__id=2).order_by("-bclick")[:3]
    chenggong = booksInfo.objects.filter(btype__id=3).order_by("-id")[:4]
    chenggong2 = booksInfo.objects.filter(btype__id=3).order_by("-bclick")[:4]
    wenxue = booksInfo.objects.filter(btype__id=4).order_by("-id")[:4]
    wenxue2 = booksInfo.objects.filter(btype__id=4).order_by("-bclick")[:4]
    keji = booksInfo.objects.filter(btype__id=5).order_by("-id")[:4]
    keji2 = booksInfo.objects.filter(btype__id=5).order_by("-bclick")[:4]
    jisuanji = booksInfo.objects.filter(btype__id=6).order_by("-id")[:4]
    jisuanji2 = booksInfo.objects.filter(btype__id=6).order_by("-bclick")[:4]
    # count = CartInfo.objects.filter(
    #     user_id=request.session.get('userid')).count()   'count':count,
    # # 构造上下文
    context = {'title': '首页', 'lishi': lishi,
               'wuxia': wuxia, 'chenggong': chenggong, 'wenxue': wenxue,
               'keji': keji, 'jisuanji': jisuanji,
               'lishi2': lishi2, 'wuxia2': wuxia2, 'chenggong2': chenggong2,
               'wenxue2': wenxue2, 'keji2': keji2, 'jisuanji2': jisuanji2,
               'buest_cart': 1,'page_name':0,'count':count}


    return render(request, 'rb_books/index.html', context)




#书籍列表
def booklist(request, typeid, pageid, sort):


    newbook = booksInfo.objects.all().order_by('-id')[:2]
    # 确定书籍的类型
    booktype = TypeInfo.objects.get(id=typeid)
    # 根据条件查询所有书籍
    if sort == '1':#按最新
        sumbookList = booksInfo.objects.filter(
            btype_id=typeid).order_by('-id')
    elif sort == '2':#按名子
        sumbookList = booksInfo.objects.filter(
            btype_id=typeid).order_by('btitle')
    elif sort == '3':#按点击量
        sumbookList = booksInfo.objects.filter(
            btype_id=typeid).order_by('-bclick')
    # 分页
    paginator = Paginator(sumbookList, 5)
    bookList = paginator.page(int(pageid))
    pindexlist = paginator.page_range


    # 构造上下文  'count': count,
    context = {'title': '书籍详情',  'list': 1,
               'buest_cart': 1, 'booktype': booktype,
               'newbook': newbook, 'bookList': bookList,
               'typeid': typeid, 'sort': sort,
               'pindexlist': pindexlist, 'pageid': int(pageid),
             }

    # 渲染返回结果
    return render(request, 'rb_books/list.html', context)



def detail(request,id):
    books = booksInfo.objects.get(pk=int(id))
    books.bclick=books.bclick+1
    books.save()
    # 查询当前书籍的类型   booksInfo__id 值

    booktype = books.btype

    news = books.btype.booksinfo_set.order_by('-id')[0:2]


    context={'title':books.btype.ttitle,'buest_cart':1,
             'b':books,'newbook':news,'id':id,
             'isDetail': True,'list':1,'booktype': booktype,}
    response=render(request,'rb_books/detail.html',context)


    #使用cookies记录最近浏览的书籍id

    #记录最近浏览,获取cookies
    books_ids = request.COOKIES.get('books_ids', '')
    #获取当前点击书籍id
    books_id='%d'%books.id
    #判断是否为空
    if books_ids!='':
        #分割出每个书籍id
        books_ids1=books_ids.split(',')
        #判断书籍是否已经存在于列表
        if books_ids1.count(books_id)>=1:
            books_ids1.remove(books_id)
        #在第一位添加
        books_ids1.insert(0,books_id)
        #判断列表数是否超过5个
        if len(books_ids1)>=6:
            #超过五个则删除第6个
            del books_ids1[5]
        #添加书籍id到cookies
        books_ids=','.join(books_ids1)
    else:
        #第一次添加，直接追加
        books_ids=books_id
    response.set_cookie('books_ids',books_ids)

    return response

def newsbooks(request):
    newbook = booksInfo.objects.all().order_by('-id')[:10]

    context={
        'newbook': newbook,
    }

    return render(request, 'rb_books/newsbooks.html', context)


def hotlists(request,pageid):
    newbook = booksInfo.objects.all().order_by('-id')[:2]
    sumbookList = booksInfo.objects.all().order_by('-bclick')

    paginator = Paginator(sumbookList, 10)
    bookList = paginator.page(int(pageid))
    pindexlist = paginator.page_range

    context={
        'sumbookList': sumbookList,
        'pindexlist': pindexlist,
        'pageid': int(pageid),
        'bookList': bookList,
        'newbook': newbook,
    }
    return render(request, 'rb_books/hotlists.html', context)
