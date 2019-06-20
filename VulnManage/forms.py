#coding:utf-8
'''
Created on 2019年6月20日

@author: 残源
'''

from django.forms import ModelForm
from . import models

class VulnForm(ModelForm):
    class Meta:
        model  = models.Vuln
        fields= ('name','cve','type','level','introduce','info','scopen','fix','fix_status')