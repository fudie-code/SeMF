#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''
from django.urls import path
from UserManage.views import views


urlpatterns = [
    path('userlist/',views.user_list,name='user_list'),
    path('usercreate/',views.user_create,name='usercreate'),
    path('userdelete/<str:user_id>/',views.user_delete,name='user_delete'),
    path('user_update/<str:user_id>/',views.user_update,name='user_update'),
    path('roleslist/',views.roleslist,name='roleslist'),
    path('useraction/<str:action>/<int:user_id>/',views.user_action,name='usersction'),
    
    ]