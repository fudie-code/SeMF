#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.urls import path
from .views import views,assetviews,portsviews,pluginsviews,sqlviews,osviews,webinfoviews,fileviews,vulnviews,chartviews

urlpatterns = [
    path('assetlist/',views.mainlist,name='assetlist'),
    path('assettypelist/',views.typelist,name='assettypelist'),
    path('assettypeinfolist/<str:asset_id>/',views.assettypeinfolist,name='assettypeinfolist'),
    
    path('assetcreate/',assetviews.assetcreate,name='assetcreate'),
    path('assetdelete/<str:asset_id>/',assetviews.assetdelete,name='assetdelete'),
    path('assetupdate/<str:asset_id>/',assetviews.assetupdate,name='assetupdate'),
    path('assetdetails/<str:asset_id>/',assetviews.assetdetails,name='assetdetails'),
    
    
    path('portlist/<str:asset_id>',portsviews.portslist,name='portlist'),
    path('portcreate/<str:asset_id>',portsviews.portcreate,name='portcreate'),
    path('portdelete/<str:port_id>',portsviews.portdelete,name='portdelete'),
    path('portupdate/<str:port_id>',portsviews.portupdate,name='portupdate'),
    
    path('pluginlist/<str:asset_id>',pluginsviews.pluginslist,name='pluginlist'),
    path('plugincreate/<str:asset_id>',pluginsviews.plugincreate,name='plugincreate'),
    path('plugindelete/<str:plugin_id>',pluginsviews.plugindelete,name='plugindelete'),
    path('pluginupdate/<str:plugin_id>',pluginsviews.pluginupdate,name='pluginupdate'),
    
    
    path('sqltypelist/',sqlviews.sqltypelist,name='sqltypelist'),
    path('sqldetails/<str:asset_id>/',sqlviews.sqldetails,name='sqldetails'),
    path('sqlupdate/<str:sql_id>/',sqlviews.sqlupdate,name='sqlupdate'),
    
    
    path('ostypelist/',osviews.ostypelist,name='ostypelist'),
    path('osdetails/<str:asset_id>/',osviews.osdetails,name='osdetails'),
    path('osupdate/<str:os_id>/',osviews.osupdate,name='osupdate'),
    
    path('languagetypelist/',webinfoviews.LanguageTypelist,name='languagetypelist'),
    path('webinfodetails/<str:asset_id>/',webinfoviews.webinfodetails,name='webinfodetails'),
    path('webinfoupdate/<str:webinfo_id>/',webinfoviews.webinfoupdate,name='webinfoupdate'),
    
    path('fileslist/<str:asset_id>/',fileviews.fileslist,name='fileslist'),
    path('filecreate/<str:asset_id>/',fileviews.filecreate,name='filecreate'),
    path('filedelete/<str:file_id>/',fileviews.filedelete,name='filedelete'),
    
    
    path('vulncreate/<str:asset_id>/',vulnviews.vulncreate,name='vulncreate'),
    
    path('assettypechart/',chartviews.assettypechart,name='assettypechart'),
    path('assetvulnlevelchart/<str:asset_id>/',chartviews.assetvulnlevelchart,name='assetvulnlevelchart'),
    
    ]