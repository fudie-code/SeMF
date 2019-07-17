#coding:utf-8
'''
Created on 2019年6月21日

@author: 残源
'''
from rest_framework import serializers
from . import models


class ArticleListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='status.name')
    status_id = serializers.CharField(source='status.id')
    type = serializers.CharField(source='type.name')
    type_id = serializers.CharField(source='type.id')
    user = serializers.CharField(source='user.username')
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = models.Article
        fields= ('id','name','abstract','body','status','status_id','type','type_id','user','create_time','update_time')



class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields= "__all__"
        
class STATUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.STATUS
        fields= "__all__"
        
        
class ArticleCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleComments
        fields= "__all__"