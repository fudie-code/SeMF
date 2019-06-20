#coding:utf-8
from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Scanner)
admin.site.register(models.Policies)