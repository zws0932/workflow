# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0002_auto_20150720_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='feedback',
            field=models.TextField(max_length=100, verbose_name='\u5904\u7406\u53cd\u9988', blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='opinion',
            field=models.TextField(max_length=100, verbose_name='\u5ba1\u6279\u610f\u89c1', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(max_length=5, verbose_name='\u72b6\u6001', choices=[(b'1', b'\xe6\x96\xb0\xe5\xbb\xba\xe4\xb8\xad'), (b'2', b'\xe5\xae\xa1\xe6\x89\xb9\xe4\xb8\xad'), (b'3', b'\xe5\xa4\x84\xe7\x90\x86\xe4\xb8\xad'), (b'4', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
    ]
