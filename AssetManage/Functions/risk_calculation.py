#coding:utf-8
from TaskManage.models import Asset
from VulnManage.models import Vuln
from django.db.models import Count
from django.db.models import  Q

def get_asset_score(asset_obj):
    score = 100
    check = 5
    vuln_count = Vuln.objects.filter(asset=asset_obj).exclude(Q(fix_status__name='已修复')|Q(fix_status__name='已忽略')).values('level').annotate(number=Count('id'))
    for item in vuln_count:
        if item['number'] >= check:
            item['number'] = check
        else:
            pass
        score = score-(int(item['level'])-1)*item['number']*2
    return score


def get_root_asset_score(asset_obj):
    numerator = 0
    denominator = 0
    asset_list = Asset.objects.filter(parent=asset_obj)
    for asset_get in asset_list:
        asset_score = get_asset_score(asset_get)
        numerator = numerator + asset_score*asset_get.weight
        denominator = denominator + 100*asset_get.weight
    if denominator == 0:
        return 0
    else:
        return numerator/denominator * 100
            
    
    
    
    