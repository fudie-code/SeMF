#coding:utf-8
'''
Created on 2019年6月17日

@author: 残源
'''
from django.urls import path
from .views import views,assetviews,portsviews,pluginsviews,sqlviews,osviews,webinfoviews,fileviews,vulnviews,chartviews,csv_excuter

urlpatterns = [
    path('assetlist/',views.mainlist,name='assetlist'),
    path('assettypelist/',views.typelist,name='assettypelist'),
    path('assettypeinfolist/<str:asset_id>/',views.assettypeinfolist,name='assettypeinfolist'),
    
    path('assetcreate/',assetviews.assetcreate,name='assetcreate'),
    path('assetdelete/<str:asset_id>/',assetviews.assetdelete,name='assetdelete'),
    path('assetupdate/<str:asset_id>/',assetviews.assetupdate,name='assetupdate'),
    path('assetdetails/<str:asset_id>/',assetviews.assetdetails,name='assetdetails'),
    
    
    path('portlist/<str:asset_id>/',portsviews.portslist,name='portlist'),
    path('portcreate/<str:asset_id>/',portsviews.portcreate,name='portcreate'),
    path('portdelete/<str:port_id>/',portsviews.portdelete,name='portdelete'),
    path('portupdate/<str:port_id>/',portsviews.portupdate,name='portupdate'),
    
    path('pluginlist/<str:asset_id>/',pluginsviews.pluginslist,name='pluginlist'),
    path('plugincreate/<str:asset_id>/',pluginsviews.plugincreate,name='plugincreate'),
    path('plugindelete/<str:plugin_id>/',pluginsviews.plugindelete,name='plugindelete'),
    path('pluginupdate/<str:plugin_id>/',pluginsviews.pluginupdate,name='pluginupdate'),
    
    
    path('sqltypelist/',sqlviews.sqltypelist,name='sqltypelist'),
    path('sqldetails/<str:asset_id>/',sqlviews.sqldetails,name='sqldetails'),
    path('sqlupdate/<str:sql_id>/',sqlviews.sqlupdate,name='sqlupdate'),
    
    
    path('ostypelist/',osviews.ostypelist,name='ostypelist'),
    path('osdetails/<str:asset_id>/',osviews.osdetails,name='osdetails'),
    path('osupdate/<str:os_id>/',osviews.osupdate,name='osupdate'),
    
    path('languagetypelist/',webinfoviews.LanguageTypelist,name='languagetypelist'),
    path('webdetails/<str:asset_id>/',webinfoviews.webinfodetails,name='webdetails'),
    path('webupdate/<str:webinfo_id>/',webinfoviews.webinfoupdate,name='webupdate'),
    
    path('fileslist/<str:asset_id>/',fileviews.fileslist,name='fileslist'),
    path('filecreate/<str:asset_id>/',fileviews.filecreate,name='filecreate'),
    path('filedelete/<str:file_id>/',fileviews.filedelete,name='filedelete'),
    path('file_get/<str:file_id>/',fileviews.file_get,name='file_get'),
    #随机值鉴权下载文件
    path('file_code/<str:file_id>/',fileviews.file_code,name='file_code'),
    path('file_download/<str:checkcode>/',fileviews.file_download,name='file_download'),
    
    
    path('vulncreate/<str:asset_id>/',vulnviews.vulncreate,name='vulncreate'),
    path('vulnlist/<str:asset_id>/',vulnviews.vulnlist,name='assetvulnlist'),
    
    path('assettypechart/',chartviews.assettypechart,name='assettypechart'),
    path('assetvulnlevelchart/<str:asset_id>/',chartviews.assetvulnlevelchart,name='assetvulnlevelchart'),
    
    path('get_example_csv/', csv_excuter.csv_get_example, name='get_example_csv'),
    path('upload_csv/', csv_excuter.csv_upload_asset, name='upload_csv'),
    
    ]