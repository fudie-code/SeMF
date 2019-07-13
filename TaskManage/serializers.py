#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''

from rest_framework import serializers
from . import models

class IdlistField(serializers.CharField):
    def to_representation(self, value):
        data_list = []
        for item in value:
            data_list.append(item.id)
        return data_list

class TaskListSerializer(serializers.ModelSerializer):
    asset = IdlistField(source='asset.all')
    type_id = serializers.CharField(source='type.id')
    status_id = serializers.CharField(source='status.id')
    scanner_id = serializers.CharField(source='scanner.id')
    police_id = serializers.CharField(source='police.id')
    starttime = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    endtime = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = models.Task
        fields= ('id','name','target','type','type_id','targetinfo','status','status_id','starttime','endtime','scanner','scanner_id','police','police_id','asset','user')
        
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields= "__all__"
        
        
class STATUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.STATUS
        fields= "__all__"