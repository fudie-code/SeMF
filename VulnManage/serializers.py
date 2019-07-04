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
    type_id = serializers.CharField(source='type.id')
    type = ExterNameField()
    level_id = serializers.CharField(source='level.id')
    level = ExterNameField()
    fix_status_id = serializers.CharField(source='fix_status.id')
    fix_status = ExterNameField()
    asset_id = serializers.CharField(source='asset.id')
    asset = serializers.CharField(source='asset.key')
    create_data = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    update_data = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = models.Vuln
        fields= ('id','name','type_id','type','level_id','level','fix_status_id','fix_status','asset_id','asset','create_data','update_data')
        
        
        
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