
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
        list_get = models.Asset.objects.filter(Q(name__icontains = key)|
                                            Q(key__icontains = key)|
                                            Q(type__name__icontains = key)|
                                            Q(description__icontains = key)|
                                            Q(manage__icontains = key)|
                                            Q(telephone__icontains = key)|
                                            Q(email__icontains = key)).order_by('updatetime')
    else:
        list_get = models.Asset.objects.filter(Q(name__icontains = key)|
                                            Q(key__icontains = key)|
                                            Q(type__name__icontains = key)|
                                            Q(description__icontains = key)|
                                            Q(manage__icontains = key)|
                                            Q(telephone__icontains = key)|
                                            Q(email__icontains = key),
                                            Q(user=user)|
                                            Q(group__user=user)).order_by('updatetime')
    list_count = list_get.count()
    pg = MyPageNumberPagination()
    list_page = pg.paginate_queryset(list_get, request,'self')
    serializers_get = serializers.AssetListSerializer(instance= list_page,many=True)
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
    serializers_get = serializers.AssetTypeSerializer(instance= list_get,many=True)
    data['msg'] = 'success'
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)


@api_view(['GET'])
def assettypeinfolist(request,asset_id):
    data = {
      "code": 1,
      "msg": "",
      "data": []
    }
    user = request.user
    if user.is_superuser:
        item_get = models.Asset.objects.filter(id = asset_id).first()
    else:
        item_get = models.Asset.objects.filter(id = asset_id,user = user).first()
    if item_get:
        list_get = models.TypeInfo.objects.filter(type_connect =item_get.type ).order_by('id')
        serializers_get = serializers.AssetTypeInfoSerializer(instance= list_get,many=True)
        data['code'] = 0
        data['msg'] = 'success'
        data['data'] = xssfilter(serializers_get.data)
    else:
        data['msg'] = '请检查权限'
    return JsonResponse(data)
    