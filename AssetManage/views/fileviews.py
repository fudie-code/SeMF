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
import uuid



@api_view(['GET'])
def fileslist(request,asset_id):
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
        list_get = models.File.objects.filter(name__icontains = key).order_by('updatetime')
        list_count = list_get.count()
        pg = MyPageNumberPagination()
        list_page = pg.paginate_queryset(list_get, request,'self')
        serializers_get = serializers.FileListSerializer(instance= list_page,many=True)
        data['code'] = 0
        data['msg'] = 'success'
        data['count'] = list_count
        data['data'] = xssfilter(serializers_get.data)
    else:
        data['code'] = 1
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
def filecreate(request,asset_id):
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
        form = forms.FileForm(request.POST,request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            file_info = form.cleaned_data['file_info']
            for f in files:
                file_suffix=f.name.split(".")[-1]
                name = f.name
                file_name=str(uuid.uuid1())+"."+file_suffix
                f.name = file_name
                models.File.objects.get_or_create(
                    name=name,
                    file=f,
                    file_info = file_info,
                    asset = asset_get,
                    )
            data['code'] = 0
            data['msg'] = '添加成功'
        else:
            data['msg'] = form.errors
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def filedelete(request,file_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.File.objects.filter(id = file_id).first()
    else:
        item_get = models.File.objects.filter(Q(asset__user = user)|Q(asset__group__user = user),id = file_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '端口删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)




