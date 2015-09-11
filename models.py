# -*- coding: utf-8 -*-
from django.db import models
from account.models import User


class Workorder(models.Model):
    '''工单表'''
    title = models.CharField(u'标题',max_length=30)
    description = models.TextField(u'描述', blank=True)
    creator = models.ForeignKey(User, verbose_name=u'创建人')
    auditor = models.ManyToManyField(User,related_name='workorder_auditor', verbose_name=u'审批人')
    operator = models.ManyToManyField(User,related_name='workorder_operator', verbose_name=u'执行人')
    take_time = models.IntegerField(u'需要时间')

    class Meta:
        verbose_name = u'标准工单'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.title


class Task(models.Model):
    '''任务表'''
    state_list = (
        ('0', '已拒绝'),
        ('1', '新建中'),
        ('2', '已提交'),
        ('3', '已审批'),
        ('4', '已处理'),
        ('5', '已确认'),
    )
    title = models.CharField(u'标题',max_length=30)
    description = models.TextField(u'描述')
    opinion = models.TextField(u'审批意见',blank=True,max_length=100)
    feedback = models.TextField(u'处理反馈',blank=True,max_length=100)
    creator = models.ForeignKey(User, verbose_name=u'创建人')
    type = models.ForeignKey('Workorder',verbose_name=u'任务类型')
    state = models.CharField(u'状态',default='1',max_length=5, choices=state_list)
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    expire_time = models.DateTimeField(u'期望时间')
    finish_time = models.DateTimeField(u'完成时间',auto_now=True)

    class Meta:
        verbose_name = u'任务创建'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __unicode__(self):
        return self.title