#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''

from .. import models
from VulnManage import models as vulnmodels
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import  Q
from ..Functions import risk_calculation

@api_view(['GET'])
def assettypechart(request):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_chart = models.Asset.objects.filter(is_delete=False).values('type__name').annotate(number=Count('id'))
    else:
        asset_chart = models.Asset.objects.filter(user=user,is_delete=False).values('type__name').annotate(number=Count('id'))
    if asset_chart:
        for item in asset_chart:
            data['categories'].append(item['type__name'])
            data['data'].append({'name':item['type__name'],'value':item['number']})
    return Response(data)




@api_view(['GET'])
def assetvulnlevelchart(request,asset_id):
    data = {
      "code": 0,
      "msg": "",
      'categories':[],
      'score':100,
      "data": [],
    }
    user =request.user
    if user.is_superuser:
        asset_get = models.Asset.objects.filter(id=asset_id,is_delete=False).first()
    else:
        asset_get = models.Asset.objects.filter(id=asset_id,user=user,is_delete=False).first()
    if asset_get:
        vuln_chart = vulnmodels.Vuln.objects.filter(asset=asset_get).exclude(Q(fix_status__name='已修复')|Q(fix_status__name='已忽略')).values('level__name').annotate(number=Count('id'))
        data['score'] = risk_calculation.get_asset_score(asset_get)
        for item in vuln_chart:
            data['categories'].append(item['level__name'])
            data['data'].append({'name':item['level__name'],'value':item['number']})
    return Response(data)
