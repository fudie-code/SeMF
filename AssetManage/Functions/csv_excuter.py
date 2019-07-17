# coding:utf-8
from .. import models
import csv


def csv_analysis(csvFile):
    with open(csvFile.name, 'r', encoding='UTF-8') as f:
        f_csv = csv.reader(f)
        for i, line in enumerate(f_csv):
            #print(line)
            if i == 0:
                continue
            name = line[0]
            key = line[1]
            type_name = line[2]
            type_search = models.Type.objects.filter(name=type_name).first()
            weight = line[3]
            description = line[4]
            manage = line[5]
            telephone = line[6]
            email = line[7]
            if type_search:
                asset_obj = models.Asset.objects.get_or_create(key=key)
                if asset_obj[1]:
                    asset_obj = asset_obj[0]
                    asset_obj.name = name
                    asset_obj.type = type_search
                    asset_obj.weight = weight
                    asset_obj.manage = manage
                    asset_obj.telephone = telephone
                    asset_obj.email = email
                    asset_obj.description = description
                    asset_obj.key = key
                    asset_obj_p = models.Asset.objects.filter(key=line[8]).first()
                    if asset_obj_p:
                        asset_obj.parent.add(asset_obj_p)
                    asset_obj.save()
