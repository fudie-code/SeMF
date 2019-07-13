#coding:utf-8
'''
Created on 2019年7月13日

@author: 残源
'''
from rest_framework import serializers
from . import models

class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scanner
        fields= ('id','name')
        
        
class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Policies
        fields= ('id','name')