#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''

from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models
from VulnManage import models as vulnmodels
from VulnManage import serializers

@api_view(['GET'])
def vulnlist(request,task_id):
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
        task_get = models.Task.objects.filter(id=task_id).first()
    else:
        task_get = models.Task.objects.filter(user=user,id=task_id).first()
    if task_get:
        list_get = vulnmodels.Vuln.objects.filter(task=task_get)
        list_count = list_get.count()
        pg = MyPageNumberPagination()
        list_page = pg.paginate_queryset(list_get, request,'self')
        serializers_get = serializers.VulnListSerializer(instance= list_page,many=True)
        data['msg'] = 'success'
        data['count'] = list_count
        data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)