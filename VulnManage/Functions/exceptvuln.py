#coding:utf-8
'''
Created on 2019年7月13日

@author: 残源
'''
from ..models import AdvanceVuln

def Get_except_vuln(source_type):
    except_vulns=[]
    except_vuln_list = AdvanceVuln.objects.filter(source=source_type)
    if except_vuln_list:
        for except_vuln in except_vuln_list:
            except_vulns.append(except_vuln.vuln_name)
    return except_vulns,except_vuln_list