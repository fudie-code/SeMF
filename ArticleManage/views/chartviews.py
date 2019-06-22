#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''

from .. import models
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def articletypechart(request):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_chart = models.Article.objects.filter(is_delete=False).values('type__name').annotate(number=Count('id'))
    else:
        asset_chart = models.Article.objects.filter(user=user,is_delete=False).values('type__name').annotate(number=Count('id'))
    if asset_chart:
        for item in asset_chart:
            data['categories'].append(item['type__name'])
            data['data'].append({'name':item['type__name'],'value':item['number']})
    return Response(data)


@api_view(['GET'])
def articlestatuschart(request):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_chart = models.Article.objects.filter(is_delete=False).values('status__name').annotate(number=Count('id'))
    else:
        asset_chart = models.Article.objects.filter(user=user,is_delete=False).values('status__name').annotate(number=Count('id'))
    if asset_chart:
        for item in asset_chart:
            data['categories'].append(item['status__name'])
            data['data'].append({'name':item['status__name'],'value':item['number']})
    return Response(data)


