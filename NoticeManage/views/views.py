#coding:utf-8

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models
from .. import serializers



@api_view(['GET'])
def noticelist(request):
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
    list_get = models.Notice.objects.filter(user=user)
    list_count = list_get.count()
    pg = MyPageNumberPagination()
    list_page = pg.paginate_queryset(list_get, request,'self')
    serializers_get = serializers.NoticeSerializer(instance= list_page,many=True)
    data['code'] = 0
    data['msg'] = 'success'
    data['count'] = list_count
    data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)