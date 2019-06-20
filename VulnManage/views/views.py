#coding:utf-8

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models
from django.db.models import  Q
from .. import serializers



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
        list_get = models.Vuln.objects.filter(Q(name__icontains = key)|
                                            Q(cve__icontains = key)|
                                            Q(level__name__icontains = key)|
                                            Q(fix_status__name__icontains = key)|
                                            Q(type__name__icontains = key)).order_by('update_data')
    else:
        list_get = models.Vuln.objects.filter(Q(name__icontains = key)|
                                            Q(cve__icontains = key)|
                                            Q(level__name__icontains = key)|
                                            Q(fix_status__name__icontains = key)|
                                            Q(type__name__icontains = key),
                                            Q(asset__user=user)|
                                            Q(asset__group__user=user)).order_by('update_data')
    list_count = list_get.count()
    pg = MyPageNumberPagination()
    list_page = pg.paginate_queryset(list_get, request,'self')
    serializers_get = serializers.VulnListSerializer(instance= list_page,many=True)
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
    serializers_get = serializers.VulnTypeSerializer(instance= list_get,many=True)
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
    #user = request.user
    list_get = models.Type.objects.all().order_by('id')
    serializers_get = serializers.VulnSTATUSSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)


@api_view(['GET'])
def levellist(request):
    data = {
      "code": 0,
      "msg": "",
      "data": []
    }
    #user = request.user
    list_get = models.Type.objects.all().order_by('id')
    serializers_get = serializers.VulnLEVELSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)
