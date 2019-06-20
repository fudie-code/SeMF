#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import xssfilter
from .. import models,forms
from django.db.models import  Q
from .. import serializers


@api_view(['GET'])
def vulndelete(request,vuln_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Vuln.objects.filter(id = vuln_id).first()
    else:
        item_get = models.Vuln.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = vuln_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '端口删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
def vulnupdate(request,vuln_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Vuln.objects.filter(id = vuln_id).first()
    else:
        item_get = models.Vuln.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = vuln_id).first()
    if item_get:
        form = forms.VulnForm(request.POST,instance=item_get)
        if form.is_valid():
            form.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = form.errors
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def vulndetails(request,vuln_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Vuln.objects.filter(id = vuln_id).first()
    else:
        item_get = models.Vuln.objects.filter(Q(asset__user=user)|Q(asset__group__user=user),id = vuln_id).first()
    if item_get:
        data_get = serializers.VulnListSerializer(instance= item_get)
        data['data'] = xssfilter(data_get.data)
        data['code'] = 0
        data['msg'] = 'success'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)




