#coding:utf-8
'''
Created on 2019年6月21日

@author: 残源
'''


from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes
from .. import models,forms
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
from django.views.decorators.csrf import csrf_protect
import uuid
from SeMF.settings import WEB_URL

@api_view(['POST'])
@csrf_protect
def filecreate(request):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": ''
    }
    #user = request.user
    form = forms.FileForm(request.POST,request.FILES)
    if form.is_valid():
        files = request.FILES.getlist('file')
        file_info = form.cleaned_data['file_info']
        for f in files:
            file_suffix=f.name.split(".")[-1]
            name = f.name
            file_name=str(uuid.uuid1())+"."+file_suffix
            f.name = file_name
            file_get = models.ArticleFile.objects.get_or_create(
                name=name,
                file=f,
                file_info = file_info,
                )
            file_get = file_get[0]
        data['code'] = 0
        data['msg'] = '添加成功'
        data['data'] = WEB_URL +'/article/fileget/'+ str(file_get.id) +'/'
    else:
        data['msg'] = '请检查参数'
    return JsonResponse(data)


@api_view(['GET'])
@permission_classes((AllowAny,))
def fileget(request,file_id):
    data = {
      "code": 1,
      "msg": "",
      "data": []
    }
    file_get = models.ArticleFile.objects.filter(id=file_id).first()
    if file_get:
        file_path = file_get.file.path
        file=open(file_path,'rb')
        response =FileResponse(file)
        response['Content-Type']='application/octet-stream'
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_get.name))
        data['code'] = 0
        data['msg'] = file_get.name + '授权成功'
        return response
    else:
        data['msg'] = '文件不存在'
    return JsonResponse(data)
    