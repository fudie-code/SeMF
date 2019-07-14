#coding:utf-8
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models
from django.db.models import  Q
from .. import serializers
from AdvanceManage import serializers as advanceserializers
from AdvanceManage import models as advancemodels




@api_view(['GET'])
def mainlist(request):
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
        list_get = models.Task.objects.filter(Q(name__icontains = key)|
                                            Q(target__icontains = key)|
                                            Q(type__name__icontains = key)|
                                            Q(status__name__icontains = key)|
                                            Q(asset__name__icontains = key)).order_by('-endtime')
    else:
        list_get = models.Task.objects.filter(Q(name__icontains = key)|
                                           Q(target__icontains = key)|
                                            Q(type__name__icontains = key)|
                                            Q(status__name__icontains = key)|
                                            Q(asset__name__icontains = key),
                                            Q(asset__user=user)|
                                            Q(asset__group__user=user)).order_by('-endtime')
    list_count = list_get.count()
    pg = MyPageNumberPagination()
    list_page = pg.paginate_queryset(list_get, request,'self')
    serializers_get = serializers.TaskListSerializer(instance= list_page,many=True)
    data['msg'] = 'success'
    data['count'] = list_count
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)



@api_view(['GET'])
def typelist(request):
    data = {
      "code": 0,
      "msg": "",
      "data": []
    }
    #user = request.user
    list_get = models.Type.objects.all().order_by('id')
    serializers_get = serializers.TypeSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)


@api_view(['GET'])
def statuslist(request):
    data = {
      "code": 0,
      "msg": "",
      "data": []
    }
    list_get = models.STATUS.objects.all().order_by('id')
    serializers_get = serializers.STATUSSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)

@api_view(['GET'])
def scannerlist(request):
    data = {
      "code": 0,
      "msg": "",
      "data": []
    }
    #user = request.user
    list_get = advancemodels.Scanner.objects.all().order_by('id')
    serializers_get = advanceserializers.ScannerSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)


@api_view(['GET'])
def policieslist(request):
    data = {
      "code": 0,
      "msg": "",
      "data": []
    }
    #user = request.user
    list_get = advancemodels.Policies.objects.all().order_by('id')
    serializers_get = advanceserializers.ScannerSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)