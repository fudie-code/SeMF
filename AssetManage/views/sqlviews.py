#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import xssfilter
from .. import models,forms
from .. import serializers
from django.db.models import  Q
from django.views.decorators.csrf import csrf_protect



@api_view(['GET'])
def sqltypelist(request):
    data = {
      "code": 0,
      "msg": "",
      "data": []
    }
    list_get = models.SQLType.objects.all().order_by('id')
    serializers_get = serializers.SQLtypeSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)



@api_view(['GET'])
def sqldetails(request,asset_id):
    data = {
      "code": 1,
      "msg": "",
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Asset.objects.filter(id = asset_id).first()
    else:
        item_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id = asset_id).first()
    if item_get:
        sql_get = models.SQLInfo.objects.get_or_create(asset=item_get)
        sql_get = sql_get[0]
        data_get = serializers.SQLSerializer(instance= sql_get)
        data['data'] = xssfilter(data_get.data)
        data['code'] = 0
        data['msg'] = 'success'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)



@api_view(['POST'])
@csrf_protect
def sqlupdate(request,sql_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.SQLInfo.objects.filter(id = sql_id).first()
    else:
        item_get = models.SQLInfo.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = sql_id).first()
    if item_get:
        form = forms.SQLInfoForm(request.POST,instance=item_get)
        if form.is_valid():
            form.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = '请检查参数'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)