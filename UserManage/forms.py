#coding:utf-8
'''
Created on 2018年10月29日

@author: 
'''

from django import forms
from django.forms import ModelForm
from RBAC import models as rbacmodels

class UserCreateForm(forms.Form):
    username = forms.CharField(label='账号',max_length=75)
    password = forms.CharField(label='密码',max_length=75)
    repassword = forms.CharField(label='重复密码',max_length=75)
    email = forms.EmailField(label='邮箱')
    mobilephone = forms.CharField(label='手机号码')
    roles = forms.CharField(label='角色',max_length=75)
    
    
class UserUpdateForm(forms.Form):
    email = forms.EmailField(label='邮箱')
    mobilephone = forms.CharField(label='手机号码')
    roles = forms.CharField(label='角色',max_length=75)
    
    
class UserProfile(ModelForm):
    class Meta:
        model  = rbacmodels.Profile
        fields= ('mobilephone','description','roles')