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
    state_list = (('1','新建中'),('2','审批中'),('3', '处理中'),('4', '已完成') )
    title = models.CharField(u'标题',max_length=30)
    description = models.TextField(u'描述')
    creator = models.ForeignKey(User, verbose_name=u'创建人')
    type = models.ForeignKey('Workorder',verbose_name=u'任务类型')
    state = models.CharField(max_length=5, choices=state_list)
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    expire_time = models.DateTimeField(u'期望时间')
    finish_time = models.DateTimeField(u'完成时间',auto_now=True)

    class Meta:
        verbose_name = u'任务创建'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __unicode__(self):
        return self.title


# class State(models.Model):
#     '''状态表'''
#     name = models.CharField(u'名称',max_length=30)
#     create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
#
#     class Meta:
#         verbose_name = u'当前状态'
#         verbose_name_plural = verbose_name
#         ordering = ['-create_time']
#
#     def __unicode__(self):
#         return self.name


# class Process(models.Model):
#     '''流程定义表'''
#     name = models.CharField(u'流程名称',max_length=30)
#     type = models.CharField(u'流程类型',max_length=30)
#     state = models.CharField(u'初始状态',max_length=30)
#     content = models.CharField(u'流程模型',max_length=30)
#     creator = models.ForeignKey(User,default=1, verbose_name=u'创建人')
#     create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
#
#
# class Order(models.Model):
#     '''活动实例表'''
#     process = models.ForeignKey(Process,default=1, verbose_name=u'流程')
#     creator = models.ForeignKey(User,default=1, verbose_name=u'创建人')
#     create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
#     expire_Time = models.DateTimeField(u'期望时间',auto_now_add=True)
#
#
#
# class Task(models.Model):
#     '''活动任务表'''
#     order = models.ForeignKey(Order,default=1, verbose_name=u'流程实例')
#     name = models.CharField(u'任务名称',max_length=30)
#     type = models.CharField(u'任务类型',max_length=30)
#     operator = models.ForeignKey(User,default=1, verbose_name=u'处理人')
#     create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
#     expire_time = models.DateTimeField(u'期望时间',auto_now_add=True)
#     finish_time = models.DateTimeField(u'完成时间',auto_now_add=True)





# class workflowjob(models.Model):
#
#
#
#     handler = models.CharField(u'处理人',max_length=30)
#     content = models.TextField(u'内容')
#
#
#     class Meta:
#         verbose_name = u'工单'
#         verbose_name_plural = verbose_name
#         ordering = ['-pubcreate_time']
#
#     def __unicode__(self):
#         return self.title
#
#
# class workflow(models.Model):
#     '''工作流'''
#     name = models.CharField(u'名称',max_length=30)
#     describe = models.TextField(u'描述', max_length=200, null=True)
#     state = models.CharField(u'初始状态',max_length=30)
#
#     #提醒方式
#     # 流程图
#
# class workflowstate(models.Model):
#     '''工作流状态'''
#     name = models.CharField(u'名称',max_length=30)
#     handler = models.CharField(u'处理人',max_length=30)
#     handler_type = models.CharField(u'处理人类型',max_length=30)
#     single_mode = models.CharField(u'接单方式',max_length=30)
#
#
#
# class workflowtran(models.Model):
#     '''工作流转表'''
#     name = models.CharField(u'名称',max_length=30)
#     state = models.CharField(u'初始状态',max_length=30)
#
#
#
# class workflowdisposelog(models.Model):
#     '''工作流日志'''
#     name = models.CharField(u'操作名称',max_length=30)
#     state = models.CharField(u'处理状态',max_length=30)
#     handler_time = models.DateTimeField(u'处理时间',auto_now_add=True)
#
#
# class workflow(models.Model):
#     '''工作流'''



















