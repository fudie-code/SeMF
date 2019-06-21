#coding:utf-8
from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.STATUS)
admin.site.register(models.Key)
admin.site.register(models.Type)
admin.site.register(models.Article)
admin.site.register(models.ArticleComments)
admin.site.register(models.ArticleFile)