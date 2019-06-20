#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''

from rest_framework import serializers
from . import models

class TaskListSerializer(serializers.ModelSerializer):
    starttime = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    endtime = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = models.Task
        fields= "__all__"
        depth = 1
        
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields= "__all__"
        
        
class STATUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.STATUS
        fields= "__all__"