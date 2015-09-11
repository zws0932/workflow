#-*- coding: utf-8 -*-
from django import forms
from workflow.models import *



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = ['creator']
        widgets = {
            'creator': forms.TextInput(attrs={"type":"hidden"}),
            'state': forms.TextInput(attrs={"type":"hidden"}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        #暂缺 新建工单状态字段验证

