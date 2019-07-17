# coding:utf-8
from .. import forms, models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import HttpResponse
import codecs
import csv
import os
from AssetManage.Functions import csv_excuter


@api_view(['POST'])
def csv_upload_asset(request):
    '''

    通过csv批量上传资产信息
    '''
    user = request.user
    data = {
        "code": 0,
        "msg": "",
        "data": []
    }
    if user.is_superuser:
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('file', None)
            if csv_file:
                try:
                    f1 = open(csv_file.name, 'wb')
                    for i in csv_file.chunks():
                        f1.write(i)
                    f1.close()
                    csv_excuter.csv_analysis(csv_file)
                    data['msg'] = '解析成功'
                except:
                    data['code'] = 1
                    data['msg'] = '文件格式不正确'
            else:
                data['code'] = 1
                data['msg'] = '参数错误'

            os.remove(csv_file.name)
        else:
            data['code'] = 1
            data['msg'] = '非法错误'
    else:
        data['code'] = 1
        data['msg'] = '权限不足'
    return Response(data)


@api_view(['GET'])
@permission_classes((AllowAny,))
def csv_get_example(request):
    '''
    获取csv批量上传示例
    '''
    data = {
        "code": 0,
        "msg": "",
        "data": []
    }
    response = HttpResponse(content_type="text/csv")
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment;filename=Asset_example.csv'

    writer = csv.writer(response, dialect='excel')
    rows = dict()
    rows['headers'] = ["资产名称", "唯一标识(企业标识/ip/url)", "资产类型",'资产权重', "资产说明", "负责人", "负责人电话", "负责人邮箱", "项目关联，填写资产标识"]
    rows['1'] = ["AssetName1", "url", "web应用",'1', "项目详细说明", "王XX", "156XXXX0905", "abcXXXXXX@XX.com", ""]
    rows['2'] = ["AssetName2", "129.1.12.x",'1', "数据库", "项目详细说明", "王XX", "156XXXX0905", "abcXXXXXX@XX.com", ""]
    rows['3'] = ["AssetName3", "192.168.1.x",'1', "服务器", "项目详细说明", "王XX", "156XXXX0905", "abcXXXXXX@XX.com", "url/ip"]

    for row in rows.values():
        writer.writerow(row)
    return response
