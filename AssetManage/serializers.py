#coding:utf-8
'''
Created on 2019年6月13日

@author: 残源
'''
from rest_framework import serializers
from . import models


class userlistField(serializers.CharField):
    def to_representation(self, value):
        data_list = []
        for item in value:
            data_list.append(item.username)
        return data_list
    
class parentlistField(serializers.CharField):
    def to_representation(self, value):
        data_list = []
        for item in value:
            data_list.append(item.name)
        return data_list

class ExterNameField(serializers.CharField):
    def to_representation(self, value):
        return value.name


class AssetListSerializer(serializers.ModelSerializer):
    type = ExterNameField()
    user = userlistField(source='user.all')
    parent = parentlistField(source='parent.all')
    starttime = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    updatetime = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = models.Asset
        fields= "__all__"
        
class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields= "__all__"
        
class AssetTypeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeInfo
        fields= "__all__"
        
        
class PortListSerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = models.PortInfo
        fields= "__all__"
        
        
class PluginListSerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = models.PluginInfo
        fields= "__all__"
        
        
class FileListSerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = models.File
        fields= "__all__"
        
class SQLtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SQLType
        fields= "__all__"

        
class SQLSerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = models.SQLInfo
        fields= "__all__"
        depth = 1
        
class OSTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OSType
        fields= "__all__"

class OsInfoSerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = models.OsInfo
        fields= "__all__"
        depth = 1


class LanguageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LanguageType
        fields= "__all__"
        
class WebInfoSerializer(serializers.ModelSerializer):
    updatetime = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = models.WebInfo
        fields= "__all__"
        depth = 1
