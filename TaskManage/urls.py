#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''
from django.urls import path
from .views import views,taskviews

urlpatterns = [
    path('tasklist/',views.mainlist,name='tasklist'),
    path('typelist/',views.typelist,name='typelist'),
    path('statuslist/',views.statuslist,name='statuslist'),
    
    path('taskcreate/<str:asset_id>/',taskviews.taskcreate,name='taskcreate'),
    path('taskdelete/<str:task_id>/',taskviews.taskdelete,name='taskdelete'),
    path('taskupdate/<str:task_id>/',taskviews.taskupdate,name='taskupdate'),
    path('taskdetails/<str:task_id>/',taskviews.taskdetails,name='taskdetails'),
    
    
    ]