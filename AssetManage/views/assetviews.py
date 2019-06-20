#coding:utf-8
'''
Created on 2019年6月15日

@author: 残源
'''
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .. import models,forms,serializers
from SeMF.views import xssfilter
from django.db.models import  Q


@api_view(['POST'])
def assetcreate(request):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    form = forms.AssetForm(request.POST)
    if form.is_valid():
        name_get = form.cleaned_data['name']
        type_get = form.cleaned_data['type']
        key_get = form.cleaned_data['key']
        description_get = form.cleaned_data['description']
        manage_get = form.cleaned_data['manage']
        telephone_get = form.cleaned_data['telephone']
        user_get = form.cleaned_data['user']
        email_get = form.cleaned_data['email']
        parent_get = form.cleaned_data['parent']
        asset_get = models.Asset.objects.get_or_create(key=key_get)
        if asset_get[1]:
            asset_get=asset_get[0]
            asset_get.name = name_get
            asset_get.type = type_get
            asset_get.description = description_get
            if user.is_superuser:
                asset_get.manage = manage_get
                asset_get.telephone = telephone_get
                asset_get.email = email_get
                for user_item in user_get:
                    asset_get.user.add(user_item)
            else:
                asset_get.manage = user.username
                asset_get.telephone = user.telephone
                asset_get.email = user.email
                asset_get.user.add(user)
            for parent_item in parent_get:
                asset_get.parent.add(parent_item)
            asset_get.save()
            data['code'] = 0
            data['msg'] = '添加成功'
        else:
            data['msg'] = '资产已存在，请勿重复添加'
    else:
        data['msg'] = form.errors
    return JsonResponse(data)



@api_view(['GET'])
def assetdelete(request,asset_id):
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
        item_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id = asset_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '资产删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def assetdetails(request,asset_id):
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
        item_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id = asset_id).first()
    if item_get:
        data_get = serializers.AssetListSerializer(instance= item_get)
        data['data'] = xssfilter(data_get.data)
        data['code'] = 0
        data['msg'] = 'success'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
def assetupdate(request,asset_id):
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
        item_get = models.Asset.objects.filter(Q(user=user)|Q(group__user=user),id = asset_id).first()
    if item_get:
        form = forms.AssetForm(request.POST,instance=item_get)
        if form.is_valid():
            form.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = form.errors
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)
