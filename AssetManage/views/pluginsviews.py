#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models,forms
from .. import serializers
from django.db.models import  Q
from django.views.decorators.csrf import csrf_protect



@api_view(['GET'])
def pluginslist(request,asset_id):
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
        list_get = models.PluginInfo.objects.filter(name__icontains = key,asset=asset_get).order_by('updatetime')
        list_count = list_get.count()
        pg = MyPageNumberPagination()
        list_page = pg.paginate_queryset(list_get, request,'self')
        serializers_get = serializers.PluginListSerializer(instance= list_page,many=True)
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
def plugincreate(request,asset_id):
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
        form = forms.PluginForm(request.POST)
        if form.is_valid():
            plugin_get = models.PluginInfo.objects.get_or_create(name=form.cleaned_data['name'],asset=asset_get)
            if plugin_get[1]:
                plugin_get= plugin_get[0]
                plugin_get.version = form.cleaned_data['version']
                plugin_get.plugin_info = form.cleaned_data['plugin_info']
                plugin_get.save()
                data['code'] = 0
                data['msg'] = '添加成功'
            else:
                data['msg'] = '插件已存在'
        else:
            data['msg'] = '请检查参数'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def plugindelete(request,plugin_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.PluginInfo.objects.filter(id = plugin_id).first()
    else:
        item_get = models.PluginInfo.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = plugin_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '插件删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
@csrf_protect
def pluginupdate(request,plugin_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.PluginInfo.objects.filter(id = plugin_id).first()
    else:
        item_get = models.PluginInfo.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = plugin_id).first()
    if item_get:
        form = forms.PluginForm(request.POST,instance=item_get)
        if form.is_valid():
            form.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = '请检查参数'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)




