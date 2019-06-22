#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''
from django.urls import path
from .views import views

urlpatterns = [
    path('noticelist/',views.noticelist,name='noticelist'),

    ]