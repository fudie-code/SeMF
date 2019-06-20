#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''
from django.urls import path
from .views import views,vulnviews

urlpatterns = [
    path('vulnlist/',views.mainlist,name='vulnlist'),
    path('typelist/',views.typelist,name='typelist'),
    path('statuslist/',views.statuslist,name='statuslist'),
    path('levellist/',views.levellist,name='levellist'),
    
    
    path('vulndelete/<str:vuln_id>/',vulnviews.vulndelete,name='vulndelete'),
    path('vulnupdate/<str:vuln_id>/',vulnviews.vulnupdate,name='vulnupdate'),
    path('vulndetails/<str:vuln_id>/',vulnviews.vulndetails,name='vulndetails'),
    
    ]