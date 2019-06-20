#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''
from django.forms import ModelForm
from . import models

class TaskForm(ModelForm):
    class Meta:
        model  = models.Task
        fields= ('name','type','targetinfo','scanner','police','asset')