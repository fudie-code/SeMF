#coding:utf-8
'''
Created on 2019年6月15日

@author: 残源
'''
from django.forms import ModelForm
from . import models
from django import forms

class AssetForm(ModelForm):
    class Meta:
        model  = models.Asset
        fields = ('name','type','key','description','manage','telephone','email','user','parent')
        
        
class AssetUpdateForm(ModelForm):
    class Meta:
        model  = models.Asset
        fields = ('name','type','description','manage','telephone','email','user','parent')
        
        
        
class PortForm(ModelForm):
    class Meta:
        model  = models.PortInfo
        fields= ('port','name','product','version','port_info')
        
class PluginForm(ModelForm):
    class Meta:
        model  = models.PluginInfo
        fields= ('name','version','plugin_info')
        
class SQLInfoForm(ModelForm):
    class Meta:
        model  = models.SQLInfo
        fields= ('key','os','version','cycle')
        
class OsInfoForm(ModelForm):
    class Meta:
        model  = models.OsInfo
        fields= ('key','hostname','os','cpu_num','memory','disk')
        
class WebInfoForm(ModelForm):
    class Meta:
        model  = models.WebInfo
        fields= ('key','middleware','middleware_version','language','web_framwork','web_framwork_version')

class FileForm(ModelForm):
    class Meta:
        model  = models.SQLInfo
        fields= ('file','file_info')