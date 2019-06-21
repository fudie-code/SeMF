#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''

from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import xssfilter
from .. import models,forms
from django.db.models import  Q
from .. import serializers
from django.db.models import Count
from django.views.decorators.csrf import csrf_protect


@api_view(['POST'])
@csrf_protect
def taskcreate(request):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    form = forms.TaskForm(request.POST)
    if form.is_valid():
        check =False
        if user.is_superuser:
            check = True
        else:
            asset_list_get = form.cleaned_data['asset']
            if asset_list_get.Count() == asset_list_get.filter(Q(user=user)|Q(group__user = user)).Count():
                check =True
        if check:
            task_get = form.save()
            task_get.user = user
            task_get.status = models.STATUS.objects.filter(name ='待执行').first()
            task_get.save()
            data['code'] = 0
            data['msg'] = 'success'
        else:
            data['msg'] = '请选择资产是否授权'
    else:
        data['msg'] = form.errors
    return JsonResponse(data)


@api_view(['GET'])
def taskdelete(request,task_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Task.objects.filter(id = task_id).first()
    else:
        item_get = models.Task.objects.filter(user=user,id = task_id).first()
    if item_get:
        item_get.delete()
        data['code'] = 0
        data['msg'] = '端口删除成功'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['POST'])
@csrf_protect
def taskupdate(request,task_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Task.objects.filter(id = task_id).first()
    else:
        item_get = models.Task.objects.filter(user=user,id = task_id).first()
    if item_get:
        form = forms.TaskForm(request.POST,instance=item_get)
        if form.is_valid():
            check =False
            asset_list_get = form.cleaned_data['asset']
            if asset_list_get.Count() == asset_list_get.filter(Q(user=item_get.user)|Q(group__user = item_get.user)).Count():
                check =True
            if check:
                task_get = form.save()
                task_get.status = models.STATUS.objects.filter(name ='待执行').first()
                task_get.save()
                data['code'] = 0
                data['msg'] = 'success'
            else:
                data['msg'] = '请选择资产是否授权给用户'
        else:
            data['msg'] = form.errors
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)


@api_view(['GET'])
def taskdetails(request,task_id):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Task.objects.filter(id = task_id).first()
    else:
        item_get = models.Task.objects.filter(user=user,id = task_id).first()
    if item_get:
        data_get = serializers.TaskListSerializer(instance= item_get)
        data['data'] = xssfilter(data_get.data)
        data['code'] = 0
        data['msg'] = 'success'
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)