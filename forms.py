#-*- coding: utf-8 -*-
from django import forms
from workflow.models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ['opinion','feedback']
        widgets = {
            'creator': forms.TextInput(attrs={"type":"hidden"}),
            'state': forms.TextInput(attrs={"type":"hidden"}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        #暂缺 新建工单状态字段验证


class ApprovalForm(forms.ModelForm):
    '''任务审批'''
    state_list = (
        ('0', '已拒绝'),
        ('3', '已审批'),
    )
    state = forms.CharField(label='状态',max_length=3,widget=forms.Select(choices=state_list))
    class Meta:
        model = Task
        fields = ['title','description','opinion','state']
        # exclude = ['creator']
        widgets = {
            'title': forms.TextInput(attrs={"readonly":"true","style":"background-color:#EEE"}),
            'description': forms.Textarea(attrs={"readonly":"true","style":"background-color:#EEE"}),
            # 'state': forms.TextInput(attrs={"type":"hidden"}),
        }

    def __init__(self, *args, **kwargs):
        super(ApprovalForm, self).__init__(*args, **kwargs)


# class HandleForm(forms.ModelForm):
#     '''任务处理'''
#     state_list = (
#         ('0', '已拒绝'),
#         ('4', '已处理'),
#     )
#     state = forms.CharField(label='状态',max_length=3,widget=forms.Select(choices=state_list))
#
#     class Meta:
#         model = Task
#         fields = ['feedback','state']
#
#     def __init__(self, *args, **kwargs):
#         super(HandleForm, self).__init__(*args, **kwargs)