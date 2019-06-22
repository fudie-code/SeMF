#coding:utf-8
'''
Created on 2019年6月22日

@author: 残源
'''

from rest_framework import serializers
from . import models


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields= "__all__"