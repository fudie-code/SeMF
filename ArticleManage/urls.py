#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''
from django.urls import path
from .views import views,articleviews,fileviews,commentsviews,chartviews

urlpatterns = [
    path('articlelist/',views.mainlist,name='articlelist'),
    path('orderlist/',views.orderlist,name='orderlist'),
    path('typelist/',views.typelist,name='typelist'),
    path('statuslist/',views.statuslist,name='statuslist'),
    
    path('articlecreate/',articleviews.articlecreate,name='articlecreate'),
    path('articledelete/<str:article_id>/',articleviews.articledelete,name='articledelete'),
    path('articleupdate/<str:article_id>/',articleviews.articleupdate,name='articleupdate'),
    path('articledetails/<str:article_id>/',articleviews.articledetails,name='articledetails'),
    
    path('articlestatuschange/<str:article_id>/<str:status_id>/',articleviews.articlestatuschange,name='articlestatuschange'),
    
    
    path('filecreate/',fileviews.filecreate,name='filecreate'),
    path('fileget/<str:file_id>/',fileviews.fileget,name='fileget'),
    
    path('commentlist/<str:article_id>/',commentsviews.commentlist,name='commentlist'),
    path('commentcreate/<str:article_id>/',commentsviews.commentcreate,name='commentcreate'),
    
    
    path('articlestatuschart/',chartviews.articlestatuschart,name='articlestatuschart'),
    path('articletypechart/',chartviews.articletypechart,name='articletypechart'),
    ]