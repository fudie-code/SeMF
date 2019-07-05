#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''

from .. import models
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import  Q

@api_view(['GET'])
def vulntypechart(request):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_chart = models.Vuln.objects.all().values('type__name').annotate(number=Count('id'))
    else:
        asset_chart = models.Vuln.objects.filter(Q(asset__user=user)|Q(asset__group__user=user)).values('type__name').annotate(number=Count('id'))
    if asset_chart:
        for item in asset_chart:
            data['categories'].append(item['type__name'])
            data['data'].append({'name':item['type__name'],'value':item['number']})
    return Response(data)


@api_view(['GET'])
def vulnstatuschart(request):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_chart = models.Vuln.objects.all().values('fix_status__name').annotate(number=Count('id'))
    else:
        asset_chart = models.Vuln.objects.filter(Q(asset__user=user)|Q(asset__group__user=user)).values('fix_status__name').annotate(number=Count('id'))
    if asset_chart:
        for item in asset_chart:
            data['categories'].append(item['fix_status__name'])
            data['data'].append({'name':item['fix_status__name'],'value':item['number']})
    return Response(data)


@api_view(['GET'])
def vulnslevelchart(request):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_chart = models.Vuln.objects.all().values('level__name').annotate(number=Count('id'))
    else:
        asset_chart = models.Vuln.objects.filter(Q(asset__user=user)|Q(asset__group__user=user)).values('level__name').annotate(number=Count('id'))
    if asset_chart:
        for item in asset_chart:
            data['categories'].append(item['level__name'])
            data['data'].append({'name':item['level__name'],'value':item['number']})
    return Response(data)