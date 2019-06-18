#coding:utf-8
'''
Created on 2018年10月29日

@author: 残源
'''
from django.http import HttpResponseRedirect
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from django.middleware import csrf
from django.utils.html import escape
import re

def index(request):
    return HttpResponseRedirect('/static/spa/index.html')


def get_token(request):
    json_data = {
      "code": 0
      ,"msg": ""
      ,"data": {}
    }
    token = csrf.get_token(request)
    json_data['data']['token']=token
    return JsonResponse(json_data)

def checkpsd(passwd):  
    p = re.match(r'^(?=.*?\d)(?=.*?[a-zA-Z]).{6,}$',passwd)
    if p:  
        return True  
    else:  
        return False
    

def checkip(ip):  
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
    if p.match(ip):  
        return True  
    else:  
        return False
    
def checkurl(url):  
    p = re.compile(r'^https?:/{2}\w.+$')
    if p.match(url):  
        return True  
    else:  
        return False
    
def checkips(str_get):
    list_get = str_get.split(';');
    for i in list_get:
        res=checkip(i)
        if res:
            return True
    return False
    

    

def checphone(phonenum):  
    p = re.match(r'^1[3458]\d{9}$',phonenum)
    if p:  
        return True  
    else:  
        return False  
    
class MyPageNumberPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 10
    #默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "limit"
    #最大页数不超过1000
    max_page_size = 100
    #获取页码数的
    page_query_param = "page"

def xssfilter(data):
    if isinstance(data,list):
        for k in data:
            k=xssfilter(k)
    elif isinstance(data,dict):
        for k,value in data.items():
            data[k]=xssfilter(value)
    else:
        data=escape(data)
    return data
        
        


 