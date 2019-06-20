#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''
from rest_framework import serializers
from . import models


class ExterNameField(serializers.CharField):
    def to_representation(self, value):
        return value.name

class VulnListSerializer(serializers.ModelSerializer):
    #type = ExterNameField()
    #level = ExterNameField()
    #fix_status = ExterNameField()
    create_data = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    update_data = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = models.Vuln
        fields= "__all__"
        depth = 1
        
        
        
class VulnTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields= "__all__"
        
        
class VulnSTATUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.STATUS
        fields= "__all__"
        
        
class VulnLEVELSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LEVEL
        fields= "__all__"