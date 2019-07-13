#coding:utf-8
from django.contrib.auth.models import User
from rest_framework.response import Response
from .. import serializers
from rest_framework.decorators import api_view
from RBAC import models
from RBAC.serializers.serializers import RoleSerializer
from .. import forms
from SeMF.views import checphone,checkpsd
from django.db.models import  Q
from AdvanceManage.Functions.many2many import many_many_addall
from SeMF.views import MyPageNumberPagination
from SeMF.views import xssfilter
from django.views.decorators.csrf import csrf_protect

# Create your views here.


@api_view(['GET'])
def user_list(request):
    user = request.user
    data = {
      "code": 0,
      "msg": "",
      "count": '',
      "data": []
    }
    key = request.GET.get('key')
    if not key:
        key=''
    if user.is_superuser:
        user_list = User.objects.filter(Q(username__icontains = key)|
                                        Q(email__icontains = key),
                                        is_superuser=False
                                        ).order_by('is_active','-date_joined')
        user_count = user_list.count()
        pg = MyPageNumberPagination()
        user_page = pg.paginate_queryset(user_list, request,'self')
        serializer_get = serializers.UserManageSerializer(instance= user_page,many=True)
        data['msg'] = 'success'
        data['count'] = user_count
        data['data'] = xssfilter(serializer_get.data)
    else:
        data['code'] = 1
        data['msg'] = '权限不足，请联系管理员'
    return Response(data)


@api_view(['POST'])
@csrf_protect
def user_create(request):
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    form = forms.UserCreateForm(request.POST)
    user = request.user
    if user.is_superuser:
        if form.is_valid():
            mobilephone=form.cleaned_data['mobilephone']
            roles=form.cleaned_data['roles']
            password = form.cleaned_data['password']
            repassword = form.cleaned_data['repassword']
            user_roles_list = models.Role.objects.filter(id__in = roles.split(','))
            if checkpsd(password):
                if password == repassword:
                    if checphone(mobilephone):
                        res = User.objects.get_or_create(
                            username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'],
                            )
                        if res[1]:
                            user_get = res[0]
                            user.profile.mobilephone=mobilephone
                            user.set_password(password)
                            user.is_active=True
                            user = many_many_addall(user_get,user_get.profile.roles,user_roles_list)
                            data['code'] = 0
                            data['msg'] = '用户创建成功'
                        else:
                            data['msg'] = '邮箱或用户名已注册'
                    else:
                        data['msg'] = '手机号不合法'
                else:
                    data['msg'] = '两次密码不一致'
            else:
                data['msg'] = '密码不符合安全规范'
        else:
            data['msg'] = '请检查输入'
    else:
        data['msg'] = '无权访问'
    return Response(data)



@api_view(['GET'])
def roleslist(request):
    data = {
      "code": 0,
      "msg": "",
      "count": '',
      "data": []
    }
    user=request.user
    key = request.GET.get('key')
    if not key:
        key=''
    if user.is_superuser:
        role_list = models.Role.objects.all().order_by('-id')
        role_count = role_list.count()
        pg = MyPageNumberPagination()
        user_page = pg.paginate_queryset(role_list, request,'self')
        serializers = RoleSerializer(instance= user_page,many=True)
        data['msg'] = 'success'
        data['count'] = role_count
        data['data'] = xssfilter(serializers.data)
    else:
        data['code'] = 1
        data['msg'] = '无权访问'
    return Response(data)


@api_view(['GET'])
def user_action(request,action,user_id):
    user = request.user
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    if user.is_superuser:
        user_get = User.objects.filter(id= user_id).first()
        if user_get and user_get.is_superuser==False:
            if user_get.is_active and action=='deny':
                user_get.is_active=False
            elif not user_get.is_active and action=='access':
                user_get.is_active=True
            user_get.save()
            data['code'] = 0
            data['msg'] = '操作成功'
        else:
            data['msg'] = '所选用户不存在或所选用户为特殊用户'
    else:
        data['msg'] = '权限错误'
    return Response(data)  
    

@api_view(['GET'])
def user_delete(request,user_id):
    user = request.user
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    if user.is_superuser:
        user_get = User.objects.filter(id= user_id).first()
        if user_get and user_get.is_superuser==False:
            user_get.delete()
            data['code'] = 0
            data['msg'] = '操作成功'
        else:
            data['msg'] = '所选用户不存在或所选用户为特殊用户'
    else:
        data['msg'] = '权限错误'
    return Response(data)



@api_view(['POST'])
def user_update(request,user_id):
    user = request.user
    data = {
      "code": 1,
      "msg": "",
      "count": '',
      "data": []
    }
    if user.is_superuser:
        user_get = User.objects.filter(id= user_id).first()
        if user_get and user_get.is_superuser==False:
            form = forms.UserUpdateForm(request.POST)
            if form.is_valid():
                user_get.profile.mobilephone = form.cleaned_data['mobilephone']
                user_get.email = form.cleaned_data['email']
                user_get.save()
                roles=form.cleaned_data['roles']
                user_roles_list = models.Role.objects.filter(id__in = roles.split(','))
                user = many_many_addall(user,user.profile.roles,user_roles_list)
                data['code'] = 0
                data['msg'] = '操作成功'
            else:
                data['msg'] = '请检查输入'
        else:
            data['msg'] = '所选用户不存在或所选用户为特殊用户'
    else:
        data['msg'] = '权限错误'
    return Response(data)