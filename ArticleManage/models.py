#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class STATUS(models.Model):
    name = models.CharField(verbose_name=u'文章状态',max_length= 100)
    descriptions = models.TextField(verbose_name=u'状态描述')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'STATUS' 
        verbose_name_plural = u'文章状态'
        
class Key(models.Model):
    name = models.CharField(verbose_name=u'文章标签',max_length= 100)
    descriptions = models.TextField(verbose_name=u'标签描述')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'key' 
        verbose_name_plural = u'文章标签'



class Type(models.Model):
    name = models.CharField(verbose_name='文章分类',max_length=30)
    body = models.TextField(verbose_name='分类简介')
    parent = models.ForeignKey('self',verbose_name=u'父菜单',related_name='parent_name',null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        # 显示层级菜单
        title_list = [self.name]
        p = self.parent
        while p:
            title_list.insert(0, p.name)
            p = p.parent
        return '-'.join(title_list)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = u'文章类型'

    

class Article(models.Model):
    name = models.CharField(verbose_name=u'文章标题', max_length=200,unique=True)
    key = models.ManyToManyField(Key,related_name='key_for_article',blank=True,verbose_name='文章分类')
    abstract = models.TextField(verbose_name=u'文章简介',null=True)
    body = models.TextField(verbose_name=u'文章内容',null=True)
    count = models.IntegerField(verbose_name='统计',default=0)
    status = models.ForeignKey(STATUS,related_name='status_for_article', on_delete=models.DO_NOTHING)
    type = models.ForeignKey(Type,related_name='type_for_article', on_delete=models.DO_NOTHING,null=True,verbose_name='文章分类')
    user = models.ForeignKey(User, related_name='article_for_user', on_delete=models.SET_NULL,null=True)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = u'知识库'
    
class ArticleComments(models.Model):
    body = models.TextField('评论内容')
    is_check = models.BooleanField('是否审核',default=False)
    comment_starttime = models.DateTimeField('添加时间',auto_now_add=True)
    
    article =  models.ForeignKey(User,related_name='articlecomment_for_article',on_delete=models.CASCADE,verbose_name='文章关联')
    user = models.ForeignKey(User,related_name='articlecomment_for_user',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment_id
    
    

class ArticleFile(models.Model):
    #article =  models.ForeignKey(User,related_name='file_for_article',on_delete=models.CASCADE,verbose_name='文章关联')
    name = models.CharField(verbose_name=u'附件名', max_length=200)
    file = models.FileField('附件内容',upload_to ='articlefiles/%Y/%m/%d/')
    file_info = models.TextField('附件说明',null=True)
    updatetime = models.DateTimeField('更新时间',auto_now=True)

    class Meta:
        verbose_name = 'ArticleFile'
        verbose_name_plural = u'知识库文件'
    