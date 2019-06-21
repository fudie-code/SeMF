#coding:utf-8
'''
Created on 2019年6月21日

@author: 残源
'''
from django.forms import ModelForm
from . import models
#from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model  = models.Article
        fields = ('name','abstract','body','type')
    
class FileForm(ModelForm):
    class Meta:
        model  = models.ArticleFile
        fields = ('file','file_info')
        
        
class CommentsForm(ModelForm):
    class Meta:
        model  = models.ArticleComments
        fields = ('body',)