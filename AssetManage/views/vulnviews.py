#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''

from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models,forms
from VulnManage import models as vulnmodels
from django.db.models import  Q
from VulnManage import serializers
from django.views.decorators.csrf import csrf_protect


@api_view(['POST'])
@csrf_protect
def vulncreate(request,asset_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        asset_get = models.Asset.objects.filter(id=asset_id).first()
    else:
        asset_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id = asset_id).first()
    if asset_get:
        form = forms.VulnForm(request.POST)
        if form.is_valid():
            vuln_get = form.save()
            vuln_get.is_check=True
            vuln_get.asset = asset_get
            vuln_get.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = form.errors
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)

@api_view(['GET'])
def vulnlist(request,asset_id):
    data = {
      "code": 0,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    key = request.GET.get('key')
    if not key:
        key=''
    if user.is_superuser:
        asset_get = models.Asset.objects.filter(id=asset_id).first()
    else:
        asset_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id=asset_id).first()
    if asset_get:
        list_get = vulnmodels.Vuln.objects.filter(asset=asset_get)
        list_count = list_get.count()
        pg = MyPageNumberPagination()
        list_page = pg.paginate_queryset(list_get, request,'self')
        serializers_get = serializers.VulnListSerializer(instance= list_page,many=True)
        data['msg'] = 'success'
        data['count'] = list_count
        data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)