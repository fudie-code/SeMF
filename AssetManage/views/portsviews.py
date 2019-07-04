#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models,forms
from django.db.models import  Q
from .. import serializers
from django.views.decorators.csrf import csrf_protect



@api_view(['GET'])
def portslist(request,asset_id):
    data = {
      "code": 1,
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
        asset_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id = asset_id).first()
    if asset_get:
        list_get = models.PortInfo.objects.filter(name__icontains = key).order_by('updatetime')
        list_count = list_get.count()
        pg = MyPageNumberPagination()
        list_page = pg.paginate_queryset(list_get, request,'self')
        serializers_get = serializers.PortListSerializer(instance= list_page,many=True)
        data['code'] = 0
        data['msg'] = 'success'
        data['count'] = list_count
        data['data'] = xssfilter(serializers_get.data)
    else:
        data['code'] = 1
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
@csrf_protect
def portcreate(request,asset_id):
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
        form = forms.PortForm(request.POST)
        if form.is_valid():
            port_get = models.PortInfo.objects.get_or_create(port=form.cleaned_data['port'],asset=asset_get)
            if port_get[1]:
                port_get= port_get[0]
                port_get.name = form.cleaned_data['name']
                port_get.name = form.cleaned_data['product']
                port_get.name = form.cleaned_data['version']
                port_get.name = form.cleaned_data['port_info']
                port_get.save()
                data['code'] = 0
                data['msg'] = '添加成功'
            else:
                data['msg'] = '组件已存在'
        else:
            data['msg'] = '请检查参数'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def portdelete(request,port_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.PortInfo.objects.filter(id = port_id).first()
    else:
        item_get = models.PortInfo.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = port_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '端口删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
@csrf_protect
def portupdate(request,port_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.PortInfo.objects.filter(id = port_id).first()
    else:
        item_get = models.PortInfo.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = port_id).first()
    if item_get:
        form = forms.PortForm(request.POST,instance=item_get)
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
def portallcheck(request,asset_id):
    #资产全端口检查
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Asset.objects.filter(id = asset_id).first()
    else:
        item_get = models.Asset.objects.filter(Q(user = user)|Q(group__user = user),id = asset_id).first()
    if item_get:
        ##添加端口检查，并更新数据文件
        data['code'] = 0
        data['msg'] = ''
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)

@api_view(['GET'])
def portcheck(request,port_id):
    #单独端口检查
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.PortInfo.objects.filter(id = port_id).first()
    else:
        item_get = models.PortInfo.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = port_id).first()
    if item_get:
        ##添加端口检查，并更新数据文件
        data['code'] = 0
        data['msg'] = '端口删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)