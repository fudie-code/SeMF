#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.urls import path
from . import views

urlpatterns = [
    path('assetlist/',views.views.mainlist,name='assetlist'),
    path('assettypelist/',views.views.typelist,name='assettypelist'),
    path('assettypeinfolist/<str:asset_id>/',views.views.assettypeinfolist,name='assettypeinfolist'),
    
    path('assetcreate/',views.assetviews.assetcreate,name='assetcreate'),
    path('assetdelete/<str:asset_id>/',views.assetviews.assetdelete,name='assetdelete'),
    path('assetupdate/<str:asset_id>/',views.assetviews.assetupdate,name='assetupdate'),
    path('assetdetails/<str:asset_id>/',views.assetviews.assetdetails,name='assetdetails'),
    
    
    path('portlist/<str:asset_id>',views.portsviews.portslist,name='portlist'),
    path('portcreate/<str:asset_id>',views.portsviews.portcreate,name='portcreate'),
    path('portdelete/<str:port_id>',views.portsviews.portdelete,name='portdelete'),
    path('portupdate/<str:port_id>',views.portsviews.portupdate,name='portupdate'),
    
    path('pluginlist/<str:asset_id>',views.pluginsviews.pluginslist,name='pluginlist'),
    path('plugincreate/<str:asset_id>',views.pluginsviews.plugincreate,name='plugincreate'),
    path('plugindelete/<str:plugin_id>',views.pluginsviews.plugindelete,name='plugindelete'),
    path('pluginupdate/<str:plugin_id>',views.pluginsviews.pluginupdate,name='pluginupdate'),
    
    
    path('sqltypelist/',views.sqlviews.sqltypelist,name='sqltypelist'),
    path('sqldetails/<str:asset_id>/',views.sqlviews.sqldetails,name='sqldetails'),
    path('sqlupdate/<str:sql_id>/',views.sqlviews.sqlupdate,name='sqlupdate'),
    
    
    path('ostypelist/',views.osviews.ostypelist,name='ostypelist'),
    path('osdetails/<str:asset_id>/',views.osviews.osdetails,name='osdetails'),
    path('osupdate/<str:os_id>/',views.osviews.osupdate,name='osupdate'),
    
    path('languagetypelist/',views.webinfoviews.LanguageTypelist,name='languagetypelist'),
    path('webinfodetails/<str:asset_id>/',views.webinfoviews.webinfodetails,name='webinfodetails'),
    path('webinfoupdate/<str:webinfo_id>/',views.webinfoviews.webinfoupdate,name='webinfoupdate'),
    
    path('fileslist/<str:asset_id>/',views.fileviews.fileslist,name='fileslist'),
    path('filecreate/<str:asset_id>/',views.fileviews.filecreate,name='filecreate'),
    path('filedelete/<str:file_id>/',views.fileviews.filedelete,name='filedelete'),
    
    ]