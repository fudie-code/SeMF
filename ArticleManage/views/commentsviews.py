#coding:utf-8
'''
Created on 2019年6月21日

@author: 残源
'''


from django.http import JsonResponse
from rest_framework.decorators import api_view
from SeMF.views import MyPageNumberPagination,xssfilter
from .. import models,forms
from .. import serializers
from django.views.decorators.csrf import csrf_protect



@api_view(['GET'])
def commentlist(request,article_id):
    data = {
      "code": 0,
      "msg": "",
      "count": '',
      "data": []
    }
    article_get = models.Article.objects.filter(id = article_id,status__name = '发布').first()
    if article_get:
        list_get = models.ArticleComments.objects.filter(asset =article_get).order_by('id')
        list_count = list_get.count()
        pg = MyPageNumberPagination()
        list_page = pg.paginate_queryset(list_get, request,'self')
        serializers_get = serializers.ArticleCommentsSerializer(instance= list_page,many=True)
        data['msg'] = 'success'
        data['count'] = list_count
        data['data'] = xssfilter(serializers_get.data)
    return JsonResponse(data)

@api_view(['POST'])
@csrf_protect
def commentcreate(request,article_id):
    data = {
      "code": 1,
      "msg": "",
      "data": []
    }
    user = request.user
    item_get = models.Article.objects.filter(id = article_id,status__name = '发布').first()
    if item_get:
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            commit_get = form.save()
            commit_get.user = user
            commit_get.article = item_get
            commit_get.save()
    else:
        data['msg']='文章不存在，或已删除'
    return JsonResponse(data)