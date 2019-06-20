#coding:utf-8

'''
Created on 2018年11月13日

@author: 残源
'''
from rest_framework import serializers
from django.contrib.auth.models import User
        
class roleslistField(serializers.CharField):
    def to_representation(self, value):
        data_list = []
        for row in value:
            data_list.append(row.name)
        return data_list
    
class IdlistField(serializers.CharField):
    def to_representation(self, value):
        data_list = []
        for item in value:
            data_list.append(item.id)
        return data_list
    
class parentlistField(serializers.CharField):
    def to_representation(self, value):
        data_list = []
        if value:
            for row in value:
                data_list.append(row.username)
        else:
            pass
        return data_list

class ExterNameField(serializers.CharField):
    def to_representation(self, value):
        return value.username      


class UserManageSerializer(serializers.ModelSerializer):
    mobilephone = serializers.CharField(source = 'profile.mobilephone')
    roles = roleslistField(source="profile.roles.all")
    parent = parentlistField(source="profile.parent.all")
    roles_id = IdlistField(source='profile.roles.all')
    class Meta:
        model = User
        fields = ('id','username','email','mobilephone','is_active','roles','roles_id')  
        
        
        