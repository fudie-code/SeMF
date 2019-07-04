#coding:utf-8
'''
Created on 2019年6月21日

@author: 残源
'''

from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import xssfilter
from .. import models,forms
from .. import serializers
from django.views.decorators.csrf import csrf_protect


@api_view(['POST'])
@csrf_protect
def articlecreate(request):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    form = forms.ArticleForm(request.POST)
    if form.is_valid():
        article_get = form.save()
        article_get.user = user
        article_get.status = models.STATUS.objects.filter(name ='新建').first()
        article_get.save()
        data['code'] = 0
        data['msg'] = 'success'
    else:
        data['msg'] = '请检查参数'
    return JsonResponse(data)


@api_view(['GET'])
def articledelete(request,article_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Article.objects.filter(id = article_id).first()
    else:
        item_get = models.Article.objects.filter(user=user,id = article_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '端口删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
@csrf_protect
def articleupdate(request,article_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Article.objects.filter(id = article_id).first()
    else:
        item_get = models.Article.objects.filter(user=user,id = article_id).first()
    if item_get:
        form = forms.ArticleForm(request.POST,instance=item_get)
        if form.is_valid():
            form.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = '请检查参数'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)

@api_view(['GET'])
def articlestatuschange(request,article_id,status_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Article.objects.filter(id = article_id).first()
        if item_get:
            item_get.status = models.STATUS.objects.filter(id =status_id ).first()
            item_get.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def articledetails(request,article_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Article.objects.filter(id = article_id).first()
    else:
        item_get = models.Article.objects.filter(status__name = '发布',id = article_id).first()
    if item_get:
        data_get = serializers.ArticleListSerializer(instance= item_get)
        data['data'] = xssfilter(data_get.data)
        data['code'] = 0
        data['msg'] = 'success'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)